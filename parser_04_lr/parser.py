from parser_04_lr.grammar import Grammar


def lr_parser(grammar: Grammar, tokens):
    buffer = []
    active = True
    while active:
        active = False

        # matching
        if len(buffer) > 0:
            pattern = tuple(e[0] for e in buffer)
            rule, size = grammar.get_rule(pattern)
            if rule:
                active = True
                del buffer[-size:]
                new_element = rule, size
                buffer.append(new_element)
                yield new_element
                continue

        # consume tokens
        if tokens is None:
            continue
        token = next(tokens)
        if token is None:
            tokens = None
            continue

        active = True
        buffer.append(token)
        yield token
    yield None
