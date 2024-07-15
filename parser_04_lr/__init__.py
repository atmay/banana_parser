from parser_04_lr.grammar import Grammar
from parser_04_lr.lexer import lexer
from parser_04_lr.parser import lr_parser
from parser_04_lr.tree_build import tree_builder


def main():
    math_grammar = Grammar({
        'E': [
            tuple('E+N'),
            tuple('E-N'),
            tuple('N'),
        ]
    })

    tree = tree_builder(lr_parser(math_grammar, lexer("N+N-N-N")))
    print(tree)


if __name__ == "__main__":
    main()
