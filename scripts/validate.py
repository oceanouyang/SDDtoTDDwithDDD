"""Validate the deliberate public file set, portable instructions, and example.

Uses only the Python standard library. It does not install or invoke upstream
skills, access remote services, or evaluate a language model's compliance.
"""

from pathlib import Path
import json
import os
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'sdd-to-tdd-with-ddd'
PUBLIC_FILES = frozenset({
    '.gitattributes',
    '.github/workflows/validate.yml',
    '.gitignore',
    'AI_CHANGELOG.md',
    'ATTRIBUTION.md',
    'CHANGELOG.md',
    'CONTRIBUTING.md',
    'LICENSE',
    'README.md',
    'README.zh-CN.md',
    'docs/compatibility.md',
    'docs/validation.md',
    'examples/loan-renewal/README.md',
    'examples/loan-renewal/loan.py',
    'examples/loan-renewal/test_loan.py',
    'scripts/validate.py',
    'skills/sdd-to-tdd-with-ddd/SKILL.md',
    'skills/sdd-to-tdd-with-ddd/agents/openai.yaml',
    'skills/sdd-to-tdd-with-ddd/references/bootstrap.md',
    'skills/sdd-to-tdd-with-ddd/references/conflicts-execution.md',
    'skills/sdd-to-tdd-with-ddd/references/conflicts-requirements.md',
    'skills/sdd-to-tdd-with-ddd/references/conflicts.md',
    'skills/sdd-to-tdd-with-ddd/references/handoffs.md',
    'skills/sdd-to-tdd-with-ddd/references/modes.md',
    'skills/sdd-to-tdd-with-ddd/references/personalization.md',
    'skills/sdd-to-tdd-with-ddd/references/verification.md',
    'skills/sdd-to-tdd-with-ddd/references/workflows.md',
})
IGNORED_DIRS = {'.git', '.venv', '__pycache__', '.validation'}
DISCLOSURE_PATTERNS = {
    'private_key': r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
    'api_secret': r'\bsk-[A-Za-z0-9_-]{20,}',
    'github_token': r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})',
    'bearer_secret': r'\bBearer\s+[A-Za-z0-9._~+/-]{20,}',
    'credential_in_url': r'https?://[^\s/@]+:[^\s/@]+@',
    'windows_absolute_path': r'(?i)\b[A-Z]:[\\/](?:Users|Program Files|workspace|projects)[\\/]',
    'unix_home_path': r'/(?:home|Users)/[A-Za-z0-9_.-]+/',
    'local_service_url': r'https?://(?:localhost|127\.0\.0\.1)(?::\d+)?',
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def source_files():
    found = set()
    for directory, folders, files in os.walk(ROOT):
        folders[:] = [name for name in folders if name not in IGNORED_DIRS]
        for name in files:
            path = Path(directory) / name
            if name.endswith(('.pyc', '.pyo')):
                continue
            found.add(path.relative_to(ROOT).as_posix())
    require(found == PUBLIC_FILES,
            'Publication file set differs: ' + json.dumps({
                'missing': sorted(PUBLIC_FILES - found),
                'unexpected': sorted(found - PUBLIC_FILES),
            }))
    return sorted(found)


def validate_metadata():
    text = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
    parts = text.split('---', 2)
    require(len(parts) == 3 and not parts[0].strip(), 'Missing skill frontmatter.')
    name = re.search(r'^name:\s*([a-z0-9-]+)\s*$', parts[1], re.M)
    description = re.search(r'^description:\s*(\S.+)\s*$', parts[1], re.M)
    require(name is not None and name[1] == SKILL.name, 'Skill identifier mismatch.')
    require(description is not None and len(name[1]) <= 64, 'Invalid skill metadata.')

    ui = (SKILL / 'agents' / 'openai.yaml').read_text(encoding='utf-8')
    fields = dict(re.findall(r'^\s{2}(\w+):\s*"([^"\n]*)"\s*$', ui, re.M))
    require(fields.get('display_name') == 'SDDtoTDDwithDDD', 'Display name mismatch.')
    require(25 <= len(fields.get('short_description', '')) <= 64, 'Invalid UI description.')
    require('$' + SKILL.name in fields.get('default_prompt', ''), 'Missing invocation.')


def validate_text_and_links(files):
    local_links = 0
    for relative in files:
        path = ROOT / relative
        require(path.stat().st_size <= 1024 * 1024, 'Unexpected large file: ' + relative)
        text = path.read_text(encoding='utf-8')
        require('\x00' not in text, 'Unexpected binary content: ' + relative)
        require('\r' not in path.read_bytes().decode('utf-8'), 'Use LF line endings: ' + relative)
        for label, pattern in DISCLOSURE_PATTERNS.items():
            require(not re.search(pattern, text), 'Possible ' + label + ' in ' + relative)
        if path.suffix != '.md':
            continue
        for target in re.findall(r'\]\(([^)]+)\)', text):
            target = target.strip('<>')
            parsed = urlsplit(target)
            if parsed.scheme:
                require(parsed.scheme == 'https', 'Unexpected link scheme in ' + relative)
                continue
            if not parsed.path:
                continue
            resolved = (path.parent / unquote(parsed.path)).resolve()
            require(resolved.is_relative_to(ROOT), 'Link escapes repository: ' + relative)
            require(resolved.is_file(), 'Missing link target in ' + relative + ': ' + target)
            if path.is_relative_to(SKILL):
                require(resolved.is_relative_to(SKILL), 'Skill is not self-contained: ' + relative)
            local_links += 1
    return local_links


def main():
    files = source_files()
    validate_metadata()
    links = validate_text_and_links(files)
    print(json.dumps({'publication_files': len(files), 'local_links': links,
                      'metadata': 'passed', 'disclosure_checks': 'passed'}, sort_keys=True), flush=True)
    result = subprocess.run(
        [sys.executable, '-B', '-m', 'unittest', 'discover', '-s', '.', '-p', 'test_*.py', '-v'],
        cwd=ROOT / 'examples' / 'loan-renewal', check=False,
    )
    require(result.returncode == 0, 'Example tests failed.')
    print('Package and example checks passed. Model compliance and automatic routing were not evaluated.')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError) as error:
        print('Validation failed: ' + str(error), file=sys.stderr)
        raise SystemExit(1)
