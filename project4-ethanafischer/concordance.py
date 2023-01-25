from __future__ import annotations

# import io
import string
from typing import TextIO

# Add more imports here as you use functions from your hash table.
from hash_table import HashTable, insert, get_item, keys, contains


def djbx33a(s: str) -> int:
    """Returns a modified DJBX33A hash of the given string.

    See the project specification for the formula.
    """
    n = min(len(s), 8)
    sum = 0
    for i in range(n):
        sum += ord(s[i]) * (33 ** (n - 1 - i))

    return 5381 * (33 ** n) + sum


def build_stop_words_table(stop_words_file: TextIO) -> HashTable:
    """Returns a hash table whose keys are the stop words.

    This will read the stop words from the file and add them to the stop
    words table.  The values stored in the table will not matter.

    Args:
        stop_words_file: the open stop words file.

    Returns:
        A hash table whose keys are the stop words.
    """
    stop_hash = HashTable(10, djbx33a)
    for word in stop_words_file:
        word = word.replace("\n", "")
        insert(stop_hash, word, 0)

    return stop_hash


def build_concordance_table(file: TextIO, stop_table: HashTable) -> HashTable:
    """Returns the concordance table for the given file.

    This will read the given file and build a concordance table
    containing all valid words in the file.

    Args:
        file: the open file to read
        stop_table: a hash table whose keys are the stop words

    Returns:
        A concordance table built from the given file.
    """

    c_hash = HashTable(10, djbx33a)

    line_count = 0
    for line in file:

        line_count += 1

        line = line.lower()
        line = line.replace("'", "")

        for c in string.punctuation:
            line = line.replace(str(c), " ")

        line = line.split()

        for word in line:
            if word.isalpha() and not contains(stop_table, word):
                if contains(c_hash, word):
                    line_list = get_item(c_hash, word)
                    if line_count != line_list[-1]:
                        line_list.append(line_count)
                    insert(c_hash, word, line_list)
                else:
                    insert(c_hash, word, [line_count])

    return c_hash


def write_concordance_table(
        file: TextIO, concordance_table: HashTable) -> None:
    """Writes the concordance table to the given file.

    This will sort the strings in the concordance table alphabetically
    and write them to the given file along with the line numbers on
    which they occurred.

    Args:
        file: the open file in which to store the table
        concordance_table: the concordance table
    """
    key_list = keys(concordance_table)
    key_list.sort()
    for key in key_list:
        line_list = get_item(concordance_table, key)
        value = " ".join(str(i) for i in line_list)
        file.write(key)
        file.write(": ")
        file.write(value)
        file.write("\n")
