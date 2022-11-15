import argparse


parser = argparse.ArgumentParser()
parser.add_argument('filename', help=' the file to read ')
parser.add_argument('--limit', '-l', type=int, help=' the number of lines to read  ')
parser.add_argument('--version', '-v', action='version', version=' %(prog)s 1.0 ')


args = parser.parse_args()

try:

    f = open(args.filename)
    limit = args.limit
# except FileNotFoundError as err:
except Exception as e:
    print(f"ERROR {e.__doc__}")
    # print(f"ERROR: {err}")
    exit(1)
else:
    with f:
        lines = f.readlines()
        lines.reverse()

        if limit:
            lines = lines[:limit]

        for line in lines:
            print(line.strip()[::-1])
