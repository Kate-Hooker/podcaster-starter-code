import argparse
from podcaster.commands import script

def main():
    parser = argparse.ArgumentParser()
    cmd_parser = parser.add_subparsers(dest='command')

    script_subparser = cmd_parser.add_parser('script')
    script_subparser.add_argument('filename', help='The filename to process', nargs='?')

    args = parser.parse_args()
    if args.command == 'script':
        script.script(args.filename)

