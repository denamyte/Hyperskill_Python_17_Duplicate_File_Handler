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
    analysis = Analysis(folder, fmt, sorting_option)
    analysis.print_sorted_by_size()
    if not h_input.check_for_duplicates():
        return
    analysis.sort_by_hash()
    analysis.print_sorted_by_hash()


if __name__ == '__main__':
    main()
