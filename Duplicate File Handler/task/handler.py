import sys
from input import HandlerInput
from analysis import Analysis


def main():
    if len(sys.argv) != 2:
        print('Directory is not specified')
        return
    folder = sys.argv[1]
    h_input = HandlerInput()
    fmt = h_input.enter_format()
    sorting_option = h_input.enter_size_option()
    Analysis(folder, fmt, sorting_option).print()


if __name__ == '__main__':
    main()
