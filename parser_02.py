from abc import ABC, abstractmethod

# grammar = Repeater( Group( Text(), Delimeter(",") )
# grammar.parse("a, b, c, d")|
# # [ "a", "b", "c", "d" ]


class Node(ABC):
    @abstractmethod
    def parse(self, text: str, cur: int = 0):
        raise NotImplementedError()
    

class Text(Node):
    def parse(self, text: str, cur: int = 0) -> tuple[int, str | None]:
        res = ''
        for i in range(cur, len(text)):
            if not text[i].isalpha():
                break
            res += text[i]
            cur += 1

        return (cur, res) if res else (cur, None)

        
class Terminal(Node):
    def __init__(self, terminal: str) -> None:
        self.terminal = terminal

    def get(self):
        return self.terminal
    
    def parse(self, text: str, cur: int = 0) -> tuple[int, str | None]:
        supposed_string = text[cur:cur + len(self.terminal)]
        if supposed_string == self.terminal:
            return (cur + len(self.terminal), supposed_string)
        return (cur, None)


class Group(Node):
    def __init__(self, *args) -> None:
        self.nodes = args

    def parse(self, text: str, cur: int = 0) -> tuple[int, str | list | None]:
        res_list = []
        index = cur
        for node in self.nodes:
            index, res = node.parse(text, index)
            if res is None:
                return (cur, None)
            res_list.append(res)
        return (index, res_list)


class Repeater(Node):
    def __init__(self, node: Node) -> None:
        self.node = node

    def parse(self, text: str, cur: int = 0) -> tuple[int, str | list | None]:
        res_list = []
        index = cur
        while True:
            index, res = self.node.parse(text, index)
            if not res:
                break
            res_list.append(res)
        
        if not res_list:
            return (cur, None)
        return (index, res_list)


if __name__=='__main__':
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
