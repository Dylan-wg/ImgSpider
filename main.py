#!/usr/bin/env python3
import argparse
import subprocess

from convertion import *
from download import *


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["download", "convert", "open", "toJPG", "rename"])
    parser.add_argument('param', nargs="*")

    args = parser.parse_args()

    try:
        if args.command == "download":
            download(args.param[0])
        elif args.command == "convert":
            convert("./", args.param[0], args.param[1])
        elif args.command == "open":
            current_dir = get_exe_dir()
            folder_path = os.path.join(current_dir, 'downloads')
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            subprocess.Popen(['explorer', folder_path])
        elif args.command == "toJPG":
            if len(args.param) == 1:
                to_jpg("./", args.param[0], delete=False)
            else:
                to_jpg("./", args.param[0], delete=(args.param[1] == "del"))
        elif args.command == "rename":
            rename("./", args.param[0], args.param[1], args.param[2], args.param[3])
    except IndexError:
        print('Fail to execute: Missing parameters')


if __name__ == "__main__":
    main()
