from collections import deque as deque

class LineChecker:
    LINE_IS_VALID = 0
    LINE_IS_CORRUPTED = 1
    
    open_close_dict = {'(':')','{':'}','[':']','<':'>'}

    def get_open_char(self, c):
        for k,v in self.open_close_dict.items():
            if c == v:
                return k

    def get_close_char(self, c):
        self.open_close_dict.get(c)

    def is_open(self, c):
        return c in self.open_close_dict.keys()

    def is_close(self, c):
        return not c in self.open_close_dict.keys()

    #if valid, returns LINE_IS_VALID
    #if corrupt, returns LINE_IS_CORRUPT, the offending character
    def check_line(self, line: str, with_errors=False):
        stack = deque()
        for line_c in line:
            if self.is_open(line_c):
                stack.append(line_c)
            else:
                stack_c = stack.pop()
                if self.get_open_char(line_c) == stack_c:
                    pass
                else:
                    if (with_errors):
                        print(f"Expected {self.get_close_char(stack_c)} but found {line_c}")
                    return self.LINE_IS_CORRUPTED, line_c


        return self.LINE_IS_VALID, None