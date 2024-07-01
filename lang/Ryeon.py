import os
import sys


class Ryeon:
    memory = [0] * 32768
    pointer = 0
    pc = 0
    code = []
    jumpTo = {}

    def increasePointer(self):
        if self.pointer >= len(self.memory) - 1:
            raise Exception("Out of memory")

        self.pointer += 1

    def decreasePointer(self):
        if self.pointer <= 0:
            raise Exception("Out of memory")

        self.pointer -= 1

    def increaseValue(self):
        self.memory[self.pointer] += 1

    def decreaseValue(self):
        self.memory[self.pointer] -= 1

    def print(self):
        sys.stdout.write(chr(self.memory[self.pointer]))

    def save(self):
        buffer = bytearray(1)
        os.read(0, buffer)
        char_code = buffer.decode("utf-8")[0]
        self.memory[self.pointer] = ord(char_code)

    def jump(self, command):
        if command == "[" and self.memory[self.pointer] == 0:  # [이고 메모리 값이 0이면
            self.pc = self.jumpTo[self.pc]  # 반복문의 끝으로 이동
        elif command == "]" and self.memory[self.pointer] != 0:  # ]이고 메모리 값이 0이 아니면
            self.pc = self.jumpTo[self.pc]  # 반복문의 시작으로 이동

    def pre_process(self):
        stack = []
        for i in range(len(self.code)):
            command = self.code[i]
            if command == "[":
                stack.append(i)
            elif command == "]":
                if len(stack) == 0:
                    raise SyntaxError("Syntax error")

                start = stack.pop()
                self.jumpTo[i] = start
                self.jumpTo[start] = i

        if len(stack) > 0:
            raise SyntaxError("Syntax error")

    def load(self, code):
        try:
            logic_code = code.split("존경하는 대리님")[1].split("제가 커피 살게요")[0]
            raw_code = logic_code.replace("\n", " ").split(" ")

            # 그래서요 : >
            # 어쩌라구요 : <
            # 왜요 : +
            # 뭐요 : -
            # 못해 : .
            # 안해 : ,
            # 하기싫어 : [
            # 집가고싶다 : ]
            for command in raw_code:
                if command == "그래서요":
                    self.code.append(">")
                elif command == "어쩌라구요":
                    self.code.append("<")
                elif command == "왜요":
                    self.code.append("+")
                elif command == "뭐요":
                    self.code.append("-")
                elif command == "못해":
                    self.code.append(".")
                elif command == "안해":
                    self.code.append(",")
                elif command == "하기싫어":
                    self.code.append("[")
                elif command == "집가고싶다":
                    self.code.append("]")

        except IndexError:
            raise SyntaxError("Syntax error : Invalid code format")



    def run(self):
        self.pre_process()

        while self.pc < len(self.code):
            command = self.code[self.pc]

            if command == ">":
                self.increasePointer()
            elif command == "<":
                self.decreasePointer()
            elif command == "+":
                self.increaseValue()
            elif command == "-":
                self.decreaseValue()
            elif command == ".":
                self.print()
            elif command == ",":
                self.save()
            elif command == "[" or command == "]":
                self.jump(command)

            self.pc += 1
