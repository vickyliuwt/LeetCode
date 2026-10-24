class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        number = ""
        operators = "+-*/"
        prevOperator = ""
        for c in s:
            if c == " ":
                continue
            elif c in operators:
                if prevOperator == "-":
                    stack.append(-int(number))
                elif prevOperator == "+":
                    stack.append(int(number))
                elif prevOperator == "*":
                    second = int(number)
                    first = int(stack.pop())
                    stack.append(first * second)
                elif prevOperator == "/":
                    second = int(number)
                    first = int(stack.pop())
                    stack.append(math.ceil(first / second) if first / second < 0 else math.floor(first / second))
                else:
                    stack.append(int(number))
                number = ""
                prevOperator = c
            else:
                number += c
        if prevOperator == "-":
            stack.append(-int(number))
        elif prevOperator == "+":
            stack.append(int(number))
        elif prevOperator == "*":
            second = int(number)
            first = int(stack.pop())
            stack.append(first * second)
        elif prevOperator == "/":
            second = int(number)
            first = int(stack.pop())
            stack.append(math.ceil(first / second) if first / second < 0 else math.floor(first / second))
        else:
            stack.append(int(number))

        return sum(stack)


        