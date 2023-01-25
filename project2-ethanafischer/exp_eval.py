from array_stack import push, pop, peek, ArrayStack


def postfix_eval(input_string: str) -> float:
    """Evaluates the given RPN expression.

    Args:
        input_string: an RPN expression

    Returns:
        The result of the expression evaluation

    Raises:
        ValueError: if the input is not well-formed
        ZeroDivisionError: if the input would cause division by zero
    """
    stack = ArrayStack()
    if not input_string:
        raise ValueError("empty input")
    ops = ["+", "-", "*", "/", "//", "^"]
    lst = input_string.split()
    for i in lst:
        try:
            i = float(i)
            push(stack, i)
        except ValueError:
            if i in ops:
                if stack.size >= 2:
                    v1 = float(pop(stack))
                    v2 = float(pop(stack))
                    if i == "+":
                        push(stack, v2 + v1)
                    elif i == "-":
                        push(stack, v2 - v1)
                    elif i == "*":
                        push(stack, v2 * v1)
                    elif i == "/":
                        try:
                            push(stack, v2 / v1)
                        except ZeroDivisionError:
                            raise ZeroDivisionError
                    elif i == "//":
                        try:
                            push(stack, v2 // v1)
                        except ZeroDivisionError:
                            raise ZeroDivisionError
                    elif i == "^":
                        push(stack, v2 ** v1)
                else:
                    raise ValueError("insufficient operands")
            else:
                raise ValueError("invalid token")

    if stack.size > 1:
        raise ValueError("too many operands")

    return float(stack.items[0])


def infix_to_postfix(input_string: str) -> str:
    """Converts the given infix string to RPN.

    Args:
        input_string: an infix expression

    Returns:
        The equivalent expression in RPN
    """
    stack = ArrayStack()
    rpn = []
    lst = input_string.split()
    for i in lst:
        try:
            float(i)
            rpn.append(i)
        except ValueError:
            if i == "(":
                push(stack, i)
            elif i == ")":
                while peek(stack) != "(":
                    rpn.append(pop(stack))
                pop(stack)
            else:
                while stack.size != 0 and precedence(i, peek(stack)):
                    rpn.append(pop(stack))
                push(stack, i)

    while stack.size != 0:
        rpn.append(pop(stack))

    return str(" ".join(rpn))


def precedence(o1, o2):
    if o1 == "^":
        p1 = 3
    elif o1 == "*" or o1 == "/" or o1 == "//":
        p1 = 2
    elif o1 == "+" or o1 == "-":
        p1 = 1

    if o2 == "^":
        p2 = 3
    elif o2 == "*" or o2 == "/" or o2 == "//":
        p2 = 2
    elif o2 == "+" or o2 == "-":
        p2 = 1
    else:
        return False

    if p2 > p1 or (p2 == p1 and o1 != "^"):
        return True
    return False
