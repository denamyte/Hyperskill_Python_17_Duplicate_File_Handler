import sys
from os import walk, path


def main():
    if len(sys.argv) != 2:
        print('Directory is not specified')
        return
    folder = sys.argv[1]
    for root, dirs, files in walk(folder):
        for f_name in files:
            print(path.join(root, f_name))


if __name__ == '__main__':
    main()
