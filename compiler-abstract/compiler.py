import re


"""
INPUT:
a = 15
b = 17
if a <= b:
    print('True')
    if a == b:
        print('Ultimate true')
else:
    print('False')


OUTPUT:
    MOV 15, A
    MOV 17, B
    CMP A B C ; сравнение A и B
    JNZ C, else
    .if-equal:
        MOV .str-are-equal, A
        CALL .print
        CMP A B C ; сравнение A и B
        JNZ C, else
        JMP if-end
    .else:
        MOV .str-not-equal, A
        CALL .print
        JMP if-end
    .end:
"""

def parser():
    pass

class Compiler:
    ASSIGNMENT = re.compile(r'(\w+)\s*=\s*(\d+)')
    COMPARISON = re.compile(r'if\s*(\w+)\s*(==|<=|>=|!=|<|>)\s*(\w+):')

    def __init__(self) -> None:
        self.stack = []
        self.result = []

    def compile(self, text: str) -> str:
        lines = text.split('\n')

        # parse one line at a time
        for line in lines:
            if match:=self.ASSIGNMENT.match(line):
                variable_name = match.group(1)
                variable_value = match.group(2)
                line_result = f'MOV {variable_value}, {variable_name}'
                self.result.append(line_result)

            if match:=self.COMPARISON.match(line):
                variable_1 = match.group(1)
                variable_2 = match.group(3)
                operator = match.group(2)
                line_result = ''
                self.result.append(line_result)


    def start_block(self):
        pass


    def end_block(self):
        pass


