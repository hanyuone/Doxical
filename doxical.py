import sys
import string

class Doxical:
    def __init__(self):
        self.co_ords = []
        self.current_grid = [0, 0]
        self.para_vars = {}
        self.output = []

        self.counter = 0
        self.value = 0

        self.errors = open("errors.txt", "r")
        self.errors = self.errors.read().splitlines()

    def call_error(self, number):
        print("[Paradox] Error #{0}: {1}".format(number + 1, self.errors[number]))
        sys.exit()

    def square_process(self):
        while "[" in self.code:
            square_start = self.code.find("[")
            square_match = 1
            square_end = 0
            for a in range(square_start + 1, len(self.code)):
                if self.code[a] == "]":
                    square_match -= 1
                    if square_match == 0:
                        square_end = a
                        break
                elif self.code[a] == "[":
                    square_match += 1
            self.code = self.code[:square_start] + self.code[square_start + 1:square_end] * input() + \
                        self.code[square_end + 1:]

    def move(self, code, number):
        self.counter = (self.counter + 1) % 10
        move_no = number + 0
        if code[0] == "^":
            self.current_grid[0] += 1
            move_no += self.counter
        elif code[0] == ">":
            self.current_grid[1] += 1
            move_no -= self.counter
        elif code[0] == "v":
            self.current_grid[0] -= 1
            move_no *= self.counter
        elif code[0] == "<":
            if self.counter == 0:
                self.call_error(0)
            self.current_grid[1] -= 1
            move_no /= self.counter
        if "/".join(str(x) for x in self.current_grid) in self.co_ords:
            self.call_error(1)
        else:
            self.co_ords.append("/".join(str(x) for x in self.current_grid))
        return [code[1:], move_no]

    def output_process(self, toggle, char):
        if toggle == "d":
            if char == "v":
                self.output.append(self.value)
            else:
                self.output.append(self.para_vars[char])
        elif toggle == "a":
            if char == "v":
                self.output.append(chr(self.value % 128))
            else:
                self.output.append(chr(self.para_vars[char] % 128))

    def paren_process(self, code):
        paren_out = code[2:code.find(")")]
        while len(paren_out) > 0:
            move_list = self.move(paren_out, self.para_vars[code[1]])
            paren_out = move_list[0]
            self.para_vars[code[1]] = move_list[1]
        return code[code.find(")") + 1:]

    def curly_process(self, code):
        curly_check = 1
        curly_end = 0
        for b in range(1, len(code)):
            if code[b] == "}":
                curly_check -= 1
                if curly_check == 0:
                    curly_end = b
                    break
            elif code[b] == "{":
                curly_check += 1
        while self.para_vars[code[1]] >= 0:
            self.process("".join(code[2:curly_end]))
        return code[curly_end + 1:]

    def process(self, code):
        process_code = code + ""
        while len(process_code) > 0:
            if process_code[0] in "^>v<":
                move_list = self.move(process_code, self.value)
                process_code = move_list[0]
                self.value = move_list[1]
            elif process_code[0] in string.uppercase:
                self.para_vars[process_code[0]] = self.value
                self.value = 0
                process_code = process_code[1:]
            elif process_code[0] in "ad":
                if len(process_code) < 2:
                    self.output_process(process_code[0], "v")
                    process_code = process_code[1:]
                elif process_code[1] == " ":
                    self.output_process(process_code[0], "v")
                    process_code = process_code[2:]
                elif process_code[1] not in string.uppercase:
                    self.output_process(process_code[0], "v")
                    process_code = process_code[1:]
                else:
                    self.output_process(process_code[0], process_code[1])
                    process_code = process_code[2:]
            elif process_code[0] == "(":
                process_code = self.paren_process(process_code)
            elif process_code[0] == "{":
                process_code = self.curly_process(process_code)

    def run_code(self, code):
        self.code = code
        self.square_process()
        self.process(self.code)
        print("".join(str(x) for x in self.output))
        
# To use, do something like this:
# run = Doxical()                       -> initiate the Doxical class
# run.run_code("{insert program here}") -> run_code is the main program to run code
