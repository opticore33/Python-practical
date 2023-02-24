# take input for number of pairs
n = int(input('Enter number of pairs:'))

stack = []
result = []

# backtrace fun
def backtrace(open_brac, close_brac):
    if open_brac == close_brac == n:
        result.append("".join(stack))
        return

    # check if open bracket is less then number of pairs
    if open_brac < n:
        stack.append("(")
        backtrace(open_brac + 1, close_brac)
        stack.pop()
        # print(stack)

    # check if close bracket is less then open bracket
    if close_brac < open_brac:
        stack.append(")")
        # print(stack)
        backtrace(open_brac, close_brac + 1)
        stack.pop()
        # print(stack)


backtrace(0, 0)
print(result)
