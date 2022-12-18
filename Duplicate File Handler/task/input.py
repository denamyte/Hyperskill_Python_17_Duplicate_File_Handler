from typing import Tuple, List


class IOHandler:
    SORTING_PROMPT = '''
Size sorting options: 
1. Descending
2. Ascending'''
    CHECK_PROMPT = '''
Check for duplicates?'''
    DELETE_FILES = '''
Delete files?'''
    SORTING_OPTIONS = ('1', '2')
    YN_OPTIONS = ('yes', 'no')
    ENTER_FILE_NUMBERS = '''
Enter file numbers to delete:'''

    @staticmethod
    def enter_format() -> str:
        return input('\nEnter file format:\n')

    @staticmethod
    def enter_sorting_option() -> int:
        return int(IOHandler.read_input_with_wrong_options(
            IOHandler.SORTING_PROMPT,
            '\nEnter a sorting option:\n',
            IOHandler.SORTING_OPTIONS))

    @staticmethod
    def check_for_duplicates() -> bool:
        return 'yes' == IOHandler.read_input_with_wrong_options(
            IOHandler.CHECK_PROMPT,
            '',
            IOHandler.YN_OPTIONS)

    @staticmethod
    def delete_files() -> bool:
        return 'yes' == IOHandler.read_input_with_wrong_options(
            IOHandler.DELETE_FILES,
            '',
            IOHandler.YN_OPTIONS)

    @staticmethod
    def read_input_with_wrong_options(prompt: str, inp: str, options: Tuple):
        print(prompt)

        while True:
            option = input(inp)
            if option in options:
                return option
            print('\nWrong option')

    @staticmethod
    def enter_file_numbers_to_delete(max_number: int) -> List[int]:
        print(IOHandler.ENTER_FILE_NUMBERS)

        while True:
            try:
                numbers = sorted(set(int(x) for x in input().split()))
                if numbers[0] < 0 or numbers[-1] > max_number:
                    raise Exception
            except:
                print('\nWrong option')
            else:
                return numbers

    @staticmethod
    def report_deleted(size: int):
        print(f'Total freed up space: {size} bytes')
