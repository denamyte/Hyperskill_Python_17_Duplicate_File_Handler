from typing import Tuple


class HandlerInput:
    SORTING_PROMPT = '''
Size sorting options: 
1. Descending
2. Ascending'''
    CHECK_PROMPT = '''
Check for duplicates?'''
    SORTING_OPTIONS = ('1', '2')
    CHECK_OPTIONS = ('yes', 'no')

    @staticmethod
    def enter_format() -> str:
        return input('\nEnter file format:\n')

    @staticmethod
    def enter_size_option() -> int:
        return int(HandlerInput.read_input_with_wrong_options(
            HandlerInput.SORTING_PROMPT,
            '\nEnter a sorting option:\n',
            HandlerInput.SORTING_OPTIONS))

    @staticmethod
    def check_for_duplicates() -> bool:
        return 'yes' == HandlerInput.read_input_with_wrong_options(
            HandlerInput.CHECK_PROMPT,
            '',
            HandlerInput.CHECK_OPTIONS)

    @staticmethod
    def read_input_with_wrong_options(prompt: str, inp: str, options: Tuple):
        print(prompt)

        while True:
            option = input(inp)
            if option in options:
                return option
            print('\nWrong option')
