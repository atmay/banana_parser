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


class Skipable(Node):
    def __init__(self, node: Node):
        self.node = node

    def parse(self, text: str, cur: int = 0) -> tuple[int, str | list | None]:
        cur, res = self.node.parse(text, cur)
        return cur, ''


class Wrapper(Node):
    def __init__(self, node: Node, handler):
        self.node = node
        self.handler = handler

    def parse(self, text: str, cur: int = 0) -> tuple[int, str | list | None]:
        cur, res = self.node.parse(text, cur)
        if res is None:
            return cur, res
        return cur, self.handler(res)


class Important(Node):
    def __init__(self, node: Node):
        self.node = node

    def parse(self, text: str, cur: int = 0) -> tuple[int, str | list | None]:
        cur, res = self.node.parse(text, cur)
        if res is None:
            print(f"Error at: {cur}, {text[cur:cur + 10]}")
        return cur, res
