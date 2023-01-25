def bears(n: int) -> bool:
    if n == 42:
        return True

    elif n < 42:
        return False

    if n % 2 == 0 and bears(n // 2):
        return True

    m = int(str(n)[-2]) * int(str(n)[-1])
    print(m)
    if (n % 3 == 0 or n % 4 == 0) and m != 0 and bears(n - m):
        return True

    if n % 5 == 0 and bears(n - 42):
        return True

    return False
