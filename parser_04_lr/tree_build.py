def tree_builder(parser):
    buffer = []
    while True:
        token = next(parser)
        if token is None:
            break
        if isinstance(token[1], int):
            token += (buffer[-token[1]:],)
            del buffer[-token[1]:]
        buffer.append(token)
    return buffer
