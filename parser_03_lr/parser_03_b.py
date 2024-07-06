def parse(grammar, tokens):
    tree = None
    buffer = []

    active = True
    while active:
        active = False

        if len(tokens) > 0:
            token = tokens.pop(0)
            buffer.append(token)
            active = True

        for head, bodies in grammar.items():
            for body in bodies:
                size = len(body)
                if size == len(buffer):
                    if match(buffer, body):
                        # Строим дерево
                        tree = (head, buffer)
                        buffer = [tree]
                        active = True
                        break
            if active:
                break

    return tree


def match(tokens, body):
    if len(tokens) == 0:
        return False
    for i in range(len(tokens)):
        if tokens[i][0] != body[i]:
            return False
    return True


def main():
    # E -> E + N | N
    grammar = {
        'E': [
            ('E', '+', 'N'),
            ('E', '-', 'N'),
            ('N',),
        ]
    }

    result = parse(grammar, [('N', 15), ('+', '+'), ('N', 37), ('-', '-'), ('N', 19)])
    print(result)


if __name__ == '__main__':
    main()
