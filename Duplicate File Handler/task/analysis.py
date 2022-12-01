from collections import defaultdict
from os import walk, path
from typing import List, Dict


class Analysis:
    def __init__(self, folder: str, fmt: str, sorting_option):
        self._folder = folder
        self._format = fmt
        self._sorting_option = sorting_option
        self._file_dict: Dict[int, List[str]] = defaultdict(list)
        self._group_by_size()
        self._sort_and_filter()

    def _group_by_size(self):
        for root, dirs, files in walk(self._folder):
            for f_name in files:
                if f_name.endswith(self._format):
                    file_path = path.join(root, f_name)
                    size = path.getsize(file_path)
                    self._file_dict[size].append(file_path)

    def _sort_and_filter(self):
        new_dict = defaultdict(list)
        for s in sorted(self._file_dict.keys(),  reverse=self._sorting_option == 1):
            if len(self._file_dict[s]) > 1:
                new_dict[s] = self._file_dict[s]
        self._file_dict = new_dict

    def print(self):
        for s in self._file_dict:
            print(f'\n{s} bytes')
            for name in self._file_dict[s]:
                print(name)
