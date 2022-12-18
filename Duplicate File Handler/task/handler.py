import sys
from input import IOHandler
from analysis import Analysis


def main():
    if len(sys.argv) != 2:
        print('Directory is not specified')
        return
    folder = sys.argv[1]
    io = IOHandler()
    fmt = io.enter_format()
    sorting_option = io.enter_sorting_option()
    analysis = Analysis(folder, fmt, sorting_option)
    analysis.print_sorted_by_size()
    if not analysis.has_sorted or not io.check_for_duplicates():
        return
    analysis.sort_by_hash()
    analysis.print_sorted_by_hash()
    dup_count = analysis.duplicate_count
    if not dup_count or not io.delete_files():
        return
    file_numbers = io.enter_file_numbers_to_delete(dup_count)
    freed_up = analysis.remove_files(file_numbers)
    io.report_deleted(freed_up)


if __name__ == '__main__':
    main()
