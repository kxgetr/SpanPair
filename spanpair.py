import argparse
import json
import sys
from pathlib import Path

def analyze(data):
    groups = {}
    for e in data:
        row = groups.setdefault(e['id'], {})
        if e['kind'] in row:
            raise ValueError('duplicate event')
        row[e['kind']] = e['time']
    return {k: v['end'] - v['start'] for k, v in groups.items()}

def main():
    parser = argparse.ArgumentParser(description='Kimliğe göre başlangıç ve bitiş olaylarından süre çıkarır.')
    parser.add_argument('file', nargs='?', help='UTF-8 JSON input file (default: stdin)')
    args = parser.parse_args()
    try:
        raw = Path(args.file).read_text(encoding='utf-8-sig') if args.file else sys.stdin.read()
        result = analyze(json.loads(raw))
        print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
    except (SyntaxError, ValueError, KeyError, TypeError, OSError, IndexError, ArithmeticError) as error:
        parser.exit(2, f'Invalid input: {error}\n')
if __name__ == '__main__':
    main()
