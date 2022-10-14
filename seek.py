"""Functions for file and directory listing

Author:
    Shota Teramoto (st707311g@gmail.com)

Licence:
    NARO NON-COMMERCIAL LICENSE AGREEMENT Version 1.0

"""

import math
import operator
import os


def walk_to_find_directories(path: str, depth: int = math.inf):
    """A function returning the generator generating the subdirectory paths.

    Args:
        path (str): Path to be explored.
        depth (int, optional): Depth of the maximum level to be explored. Defaults to unlimited.

    Yields:
        str: directory path

    Examples:
        for directory_path in walk_to_find_directories(target_directory_path):
            print(directory_path)
    """
    depth -= 1
    with os.scandir(path) as p:
        p = list(p)
        p.sort(key=operator.attrgetter("name"))
        for entry in p:
            if entry.is_dir():
                yield entry.path
            if entry.is_dir() and depth > 0:
                yield from walk_to_find_directories(entry.path, depth)


def walk_to_find_files(
    path: str, depth: int = math.inf, extension_filter: str = None
):
    """A function returning the generator generating the file paths.

    Args:
        path (str): Path to be explored.
        depth (int, optional): Depth of the maximum level to be explored. Defaults to unlimited.
        extension_filter (str, optional): Only results with extension listed in extension_filter will be returned. Defaults is no filtering.

    Yields:
        str: file path.

    Examples:
        for file_path in walk_to_find_files(target_directory_path):
            print(file_path)
    """
    depth -= 1
    with os.scandir(path) as p:
        p = list(p)
        p.sort(key=operator.attrgetter("name"))
        for entry in list(p):
            if entry.is_file():
                if extension_filter is None:
                    yield entry.path
                else:
                    if entry.path.lower().endswith(extension_filter):
                        yield entry.path

            if entry.is_dir() and depth > 0:
                yield from walk_to_find_files(
                    entry.path, depth, extension_filter
                )
