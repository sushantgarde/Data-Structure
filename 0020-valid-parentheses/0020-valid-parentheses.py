class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        top = -1

        def push(value):
            nonlocal top

            stack.append(value)
            top += 1

        def pop():
            nonlocal top

            value = stack.pop()
            top -= 1
            return value

        def is_empty():
            return top == -1

        for ch in s:

            # Opening parenthesis
            if ch == '(' or ch == '{' or ch == '[':
                push(ch)

            # Closing parenthesis
            elif ch == ')' or ch == '}' or ch == ']':

                if is_empty():
                    return False

                current_parent = pop()

                if ((ch == ')' and current_parent != '(') or
                    (ch == '}' and current_parent != '{') or
                    (ch == ']' and current_parent != '[')):
                    return False

        # Stack should be empty at the end
        return is_empty()