from __future__ import annotations
# import io

from typing import Optional, TextIO
from ordered_list import size, pop, insert, OrderedList


class HuffmanNode:
    """Represents a node in a Huffman tree.

    Attributes:
        char: The character as an integer ASCII value
        frequency: The frequency of the character in the file
        left: The left Huffman sub-tree
        right: The right Huffman sub-tree
    """

    def __init__(
            self,
            char: int,
            frequency: int,
            left: Optional[HuffmanNode] = None,
            right: Optional[HuffmanNode] = None):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right

    def __eq__(self, other) -> bool:
        """Returns True if and only if self and other are equal."""
        return (isinstance(other, HuffmanNode)
                and self.char == other.char
                and self.frequency == other.frequency
                and self.left == other.left
                and self.right == other.right
                )

    def __lt__(self, other) -> bool:
        """Returns True if and only if self < other."""
        if self.frequency == other.frequency:
            return self.char < other.char
        else:
            return self.frequency < other.frequency

    def __le__(self, other) -> bool:
        if self.frequency == other.frequency:
            return self.char <= other.char
        else:
            return self.frequency < other.frequency


# in_file = io.StringIO('a')
# out_file = io.StringIO('')
# in_file = open('text_files/empty_file.txt')
# out_file = open('out_file_test.txt', 'w')


def count_frequencies(file: TextIO) -> list[int]:
    """Reads the given file and counts the frequency of each character.

    The resulting Python list will be of length 256, where the indices
    are the ASCII values of the characters, and the value at a given
    index is the frequency with which that character occurred.
    """
    lst_freq = [0] * 256
    for line in file:
        for char in line:
            lst_freq[ord(char)] += 1
    return lst_freq


def build_huffman_tree(frequencies: list[int]) -> Optional[HuffmanNode]:
    """Creates a Huffman tree of the characters with non-zero frequency.

    Returns the root of the tree.
    """
    huffman_list = OrderedList()
    for i in range(len(frequencies)):
        if frequencies[i] > 0:
            insert(huffman_list, HuffmanNode(i, frequencies[i]))
    if size(huffman_list) == 0:
        return None
    while size(huffman_list) != 1:
        rem_1 = pop(huffman_list, 0)
        rem_2 = pop(huffman_list, 0)
        merge_freq = rem_1.frequency + rem_2.frequency
        if rem_1.char > rem_2.char:
            merge_char = rem_2.char
        else:
            merge_char = rem_1.char
        merge = HuffmanNode(merge_char, merge_freq, rem_1, rem_2)
        insert(huffman_list, merge)

    return pop(huffman_list, 0)


def create_codes(tree: Optional[HuffmanNode]) -> list[str]:
    """Traverses the tree creating the Huffman code for each character.

    The resulting Python list will be of length 256, where the indices
    are the ASCII values of the characters, and the value at a given
    index is the Huffman code for that character.
    """
    code_list = [""] * 256
    code = ''
    if tree is not None:
        traverse_tree(tree, code_list, code)
    return code_list


def traverse_tree(tree, lst, code):
    if tree.left is not None:
        traverse_tree(tree.left, lst, code + '0')
    if tree.right is not None:
        traverse_tree(tree.right, lst, code + '1')
    if tree.left is None and tree.right is None:
        lst[tree.char] = code


def create_header(frequencies: list[int]) -> str:
    """Returns the header for the compressed Huffman data.

    For example, given the file "aaabbbbcc", this would return:
    "97 3 98 4 99 2"
    """
    header = []
    for i in range(len(frequencies)):
        if frequencies[i] != 0:
            header.append(str(i))
            header.append(str(frequencies[i]))

    return " ".join(header)


def huffman_encode(in_file: TextIO, out_file: TextIO) -> None:
    """Encodes the data in the input file, writing the result to the
    output file.
    """

    freq_list = count_frequencies(in_file)
    huff_tree = build_huffman_tree(freq_list)
    code_list = create_codes(huff_tree)
    code_header = create_header(freq_list)

    out_file.write(code_header)
    out_file.write("\n")

    in_file.seek(0)

    for line in in_file:
        for char in line:
            out_file.write(code_list[ord(char)])


def parse_header(header: str) -> list[int]:
    freq_list = [0] * 256
    header_list = [int(i) for i in header.split()]
    for i in range(0, len(header_list), 2):
        freq_list[header_list[i]] = header_list[i + 1]
    return freq_list


def huffman_decode(in_file: TextIO, out_file: TextIO) -> None:
    header = in_file.readline()
    freq_list = parse_header(header)
    huffman_tree = build_huffman_tree(freq_list)
    code = in_file.readline()

    if huffman_tree is None:
        return

    if huffman_tree.left is None and huffman_tree.right is None:
        for i in range(huffman_tree.frequency):
            out_file.write(chr(huffman_tree.char))

    node = huffman_tree
    for val in code:
        if val == '0':
            node = node.left
            if node.left is None and node.right is None:
                out_file.write(chr(node.char))
                node = huffman_tree
        elif val == '1':
            node = node.right
            if node.left is None and node.right is None:
                out_file.write(chr(node.char))
                node = huffman_tree
