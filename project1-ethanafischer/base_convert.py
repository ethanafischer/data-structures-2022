def convert(num: int, base: int) -> str:
    s = ''
    digits = '0123456789ABCDEF'
    q = num // base  # quotient
    r = num % base  # remainder

    if q == 0:
        return digits[r] + s

    return convert(q, base) + digits[r]
