def parse(grammar, tokens):
    output = []
    buffer = []

    active = True
    while active:
        active = False

        if len(tokens) > 0:
            token = tokens.pop(0)
            output.append(token)
            buffer.append(token)
            active = True

        for head, bodies in grammar.items():
            for body in bodies:
                size = len(body)
                if size == len(buffer):
                    if match(buffer[-size:], body):
                        node = (head, size)
                        buffer = buffer[0:len(buffer) - size]
                        buffer.append(node)
                        output.append(node)
                        active = True
                        break
            if active:
                break

    return output


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

    # N + N - N
    result = parse(grammar, [('N', 15), ('+', '+'), ('N', 37), ('-', '-'), ('N', 19)])
    print(result)

    # TODO: разобраться почему скобки не срабатывают
    # Ожидаемый вывод:
    #   [('N', 15), ('E', 1), ('+', '+'), ('(', '('), ('N', 37), ('E', 1), ('-', '-'), ('N', 19), ('E', 3), (')', ')'), ('E', 3)]
    #   N E + ( N E - N E ) E
    # Реальный вывод:
    #   [('N', 15), ('E', 1), ('+', '+'), ('(', '('), ('N', 37), ('-', '-'), ('N', 19), (')', ')')]
    #   N E + ( N - N )

    # E -> ( E ) | E + N | N
    grammar = {
        'E': [
            ('(', 'E', ')'),
            ('E', '+', 'N'),
            ('E', '-', 'N'),
            ('N',),
        ]
    }

    # N + ( N - N )
    result = parse(grammar, [('N', 15), ('+', '+'), ('(', '('), ('N', 37), ('-', '-'), ('N', 19), (')', ')')])
    print(result)


if __name__ == '__main__':
    main()
