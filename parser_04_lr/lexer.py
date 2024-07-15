def lexer(text):
    # Yes, that's stupidest solution for tests only
    for e in text:
        yield e, e
    yield None
