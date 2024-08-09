import re


"""
INPUT:
a = 15
b = 17
if a <= b:
    print(True)
    if a == b:
        print(UltimateTrue)
        end
else:
    print(False)
    end


OUTPUT:
    MOV 15, A
    MOV 17, B
    
    ; if a <= b:
    CMP A B C
    JLEZ C, if
    JMP end
    .if-1:
        MOV .str, D
        CALL .print
        ; if a == b:
        CMP A B C ; сравнение A и B
        JZ C, if
        .if-2:
            MOV .str, D
            CALL .print
        JMP end-2
        .end-2:
    JMP end-1
    .else-1:
        MOV .str, D
        CALL .print
        JMP end-1
    .end-1:
"""


class Compiler:
    ASSIGNMENT = re.compile(r'(\w+)\s*=\s*(\d+)')
    COMPARISON = re.compile(r'if\s*(\w+)\s*(==|<=|>=|!=|<|>)\s*(\w+):')
    FUNCTION_CALL = re.compile(r'(\w+)\((\w+)\)')
    END = re.compile(r'end')
    ELSE = re.compile(r'else:')

    OPERATORS = {
        '==': "JZ",
        '!=': 'JNZ',
        '>=': 'JGEZ',
        '<=': 'JLEZ',
        '<': 'JLZ',
        '>': 'JGZ'
    }

    def __init__(self) -> None:
        self.stack = []
        self.result = []
        self.block_counter = 0
        self.current_block = 0

    def compile(self, text: str) -> str:
        lines = text.split('\n')

        # parse one line at a time
        for line in lines:
            indent = '    '*len(self.stack)

            line = line.strip()
            
            if not line:
                continue

            if match:=self.ASSIGNMENT.match(line):
                variable_name = match.group(1)
                variable_value = match.group(2)
                line_result = f'{indent}MOV {variable_value}, {variable_name}'
                self.result.append(line_result)
            
            if match:=self.COMPARISON.match(line):
                #; if a <= b:
                # CMP A B C
                # JLEZ C, if
                # JMP end
                # .if-1:
                variable_1 = match.group(1)
                variable_2 = match.group(3)
                operator = match.group(2)
                self.start_block()
                
                lines_result = [
                    f'{indent}CMP {variable_1} {variable_2} C',
                    f'{indent}{self.OPERATORS[operator]} C, if',
                    f'{indent}JMP end-{self.current_block}',
                    f'{indent}.if-{self.current_block}']
                self.result.extend(lines_result)

            if match:=self.FUNCTION_CALL.match(line):
                # MOV .str, D
                # CALL .print
                function_name = match.group(1)
                argument = match.group(2)
                lines_result = [
                    f'{indent}MOV .{argument}, D',
                    f'{indent}CALL .{function_name}'
                    ]
                self.result.extend(lines_result)

            if match:=self.END.match(line):
                # JMP end-1
                # .end-1:
                lines_result = [
                    f'{indent}JMP end-{self.current_block}',
                    f'{indent}end-{self.current_block}:'
                ]
                self.result.extend(lines_result)
                self.end_block()


            if match:=self.ELSE.match(line):
                # JMP end-1
                # .else-1:
                lines_result = [
                    f'{indent}JMP end-{self.current_block}',
                    f'{indent}else-{self.current_block}:'
                ]
                self.result.extend(lines_result)
                

    def start_block(self):
        self.block_counter += 1
        self.stack.append(self.block_counter)
        self.current_block = self.block_counter

    def end_block(self):
        self.current_block = self.stack.pop()




a = Compiler()
input = """
a = 15
b = 17
if a <= b:
    print(True)
    if a == b:
        print(UltimateTrue)
        end
else:
    print(False)
    end"""

a.compile(text=input)
print('\n'.join(a.result))