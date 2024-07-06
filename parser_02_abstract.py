from parser_02 import *


def main():
    text = Text()
    print(text.parse('abc123'))
    print(text.parse('23ASD'))

    print()
    terminal1 = Terminal(',')
    terminal2 = Terminal('text')

    print()
    print(terminal1.parse('a,asdfadsfasdf', 1))
    print(terminal1.parse('asdf'))
    print(terminal2.parse('asdfasdfastextasdfadsfasdtextf'))
    print(terminal2.parse('text'))

    print()
    group = Group(Text(), Terminal(","))
    print(group.parse('a, b, c, d', 0))
    print(group.parse('a, b, c, d', 1))
    print(group.parse('a, b, c, d', 2))
    print(group.parse('a, b, c, d', 3))
    print(group.parse('a, b, c, d', 4))

    print()
    repeater = Repeater(Group(Text(), Terminal(",")))
    print(repeater.parse('a,b,c,d', 0))

    print()
    print("GRAMMAR:")

    g_pair = Wrapper(Group(Text(), Skipable(Terminal(","))), lambda p: p[0])
    g_pairs = Repeater(g_pair)
    g_array = Wrapper(Group(Terminal("["), g_pairs, Important(Terminal("]"))), lambda g: g[1])
    grammar = Important(g_array)

    # G -> "[" pairs "]"
    # pairs -> [ pair ]
    # pair -> text ","

    # g_pairs = [ text + optional(",") ]
    # g_array = "[" + g_pairs + "]"
    # grammar = g_array | g_object | g_element

    print()
    print(grammar.parse('a,b,c,', 0))

    print()
    print(grammar.parse('[a,b,c,d]', 0))

    print()
    print(grammar.parse('[a,b,c,d,]', 0))

    print()
    print(grammar.parse('[a,b,!,d,]', 0))

    print()
    print(grammar.parse('[a,b,d,fg  444', 0))

    print()
    print(grammar.parse('{a,b,c,d}', 0))


if __name__ == '__main__':
    main()


def main():
    text = Text()
    print(text.parse('abc123'))
    print(text.parse('23ASD'))

    print()
    terminal1 = Terminal(',')
    terminal2 = Terminal('text')

    print()
    print(terminal1.parse('a,asdfadsfasdf', 1))
    print(terminal1.parse('asdf'))
    print(terminal2.parse('asdfasdfastextasdfadsfasdtextf'))
    print(terminal2.parse('text'))

    print()
    group = Group(Text(), Terminal(","))
    print(group.parse('a, b, c, d', 0))
    print(group.parse('a, b, c, d', 1))
    print(group.parse('a, b, c, d', 2))
    print(group.parse('a, b, c, d', 3))
    print(group.parse('a, b, c, d', 4))

    print()
    repeater = Repeater(Group(Text(), Terminal(",")))
    print(repeater.parse('a,b,c,d', 0))

    print()
    print("GRAMMAR:")

    g_pair = Wrapper(Group(Text(), Skipable(Terminal(","))), lambda p: p[0])
    g_pairs = Repeater(g_pair)
    g_array = Wrapper(Group(Terminal("["), g_pairs, Important(Terminal("]"))), lambda g: g[1])
    grammar = Important(g_array)

    # G -> "[" pairs "]"
    # pairs -> [ pair ]
    # pair -> text ","

    # g_pairs = [ text + optional(",") ]
    # g_array = "[" + g_pairs + "]"
    # grammar = g_array | g_object | g_element

    print()
    print(grammar.parse('a,b,c,', 0))

    print()
    print(grammar.parse('[a,b,c,d]', 0))

    print()
    print(grammar.parse('[a,b,c,d,]', 0))

    print()
    print(grammar.parse('[a,b,!,d,]', 0))

    print()
    print(grammar.parse('[a,b,d,fg  444', 0))

    print()
    print(grammar.parse('{a,b,c,d}', 0))


if __name__ == '__main__':
    main()
