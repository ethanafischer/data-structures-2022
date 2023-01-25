from __future__ import annotations


def perm_gen_lex(s: str) -> list[str]:
    new_list = []

    if s == "":
        return ['']

    for char in range(len(s)):
        t = s[:char] + s[char + 1:]
        for perm in perm_gen_lex(t):
            new_list.append(s[char] + perm)
    return new_list
