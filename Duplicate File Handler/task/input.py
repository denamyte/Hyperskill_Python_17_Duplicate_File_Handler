class HandlerInput:
    SORTING_OPTIONS = ('1', '2')

    @staticmethod
    def enter_format() -> str:
        return input('\nEnter file format:\n')

    @staticmethod
    def enter_size_option() -> int:
        print('''
Size sorting options:
1. Descending
2. Ascending''')

        while True:
            option = input('\nEnter a sorting option:\n')
            if option in HandlerInput.SORTING_OPTIONS:
                return int(option)
            print('\nWrong option')

