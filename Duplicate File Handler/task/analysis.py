import hashlib
import os.path
from collections import defaultdict
from os import walk, path
from typing import List, Dict


class Analysis:
    def __init__(self, folder: str, fmt: str, sorting_option):
        self._folder = folder
        self._format = fmt
        self._sorting_option = sorting_option
        self._file_dict: Dict[int, List[str]] = defaultdict(list)
        self._hash_dict: Dict[int, Dict[str, List[str]] ] = defaultdict(lambda: defaultdict(list))
        self._group_by_size()
        self._sort_by_size_and_filter()

    def _group_by_size(self):
        for root, dirs, files in walk(self._folder):
            for f_name in files:
                if f_name.endswith(self._format):
                    file_path = path.join(root, f_name)
                    size = path.getsize(file_path)
                    self._file_dict[size].append(file_path)

    def _sort_by_size_and_filter(self):
        new_dict = defaultdict(list)
        for s in sorted(self._file_dict.keys(),  reverse=self._sorting_option == 1):
            if len(self._file_dict[s]) > 1:
                new_dict[s] = self._file_dict[s]
        self._file_dict = new_dict

    @property
    def has_sorted(self) -> bool:
        return len(self._file_dict) > 0

    def print_sorted_by_size(self):
        for size in self._file_dict:
            print(f'\n{size} bytes')
            for name in self._file_dict[size]:
                print(name)

    def sort_by_hash(self):
        for size in self._file_dict:
            for file_name in self._file_dict[size]:
                file_dict = self._hash_dict[size]
                with open(file_name, 'rb') as file:
                    hash_str = hashlib.md5(file.read()).hexdigest()
                    file_dict[hash_str].append(file_name)

        sizes = list(self._hash_dict.keys())
        for size in sizes:
            file_dict = self._hash_dict[size]
            hashes = list(file_dict.keys())
            for h in hashes:
                if len(file_dict[h]) <= 1:
                    del file_dict[h]
            if not len(file_dict):
                del self._hash_dict[size]

    def print_sorted_by_hash(self):
        counter = 0
        for size in self._hash_dict:
            print(f'\n{size} bytes')
            file_dict = self._hash_dict[size]
            for h in file_dict:
                print(f'Hash: {h}')
                names = file_dict[h]
                for name in names:
                    counter += 1
                    print(f'{counter}. {name}')

    @property
    def duplicate_count(self) -> int:
        counter = 0
        for size in self._hash_dict:
            for h in self._hash_dict[size]:
                names = self._hash_dict[size][h]
                counter += len(names)
        return counter

    def remove_files(self, file_numbers: List[int]) -> int:
        """
        removes selected files and returns their size
        :param file_numbers the numbers of files to delete
        :return the total freed up space
        """
        file_size_sum = 0
        file_counter = 0
        for size in self._hash_dict:
            for h in self._hash_dict[size]:
                names = self._hash_dict[size][h]
                for name in names:
                    file_counter += 1
                    if file_counter in file_numbers:
                         file_size_sum += os.path.getsize(name)
                         os.remove(name)
        return file_size_sum
