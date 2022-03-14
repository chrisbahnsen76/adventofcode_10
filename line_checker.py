class line_checker:
    LINE_IS_VALID = 0
    LINE_IS_CORRUPTED = 1

    open_close_dict = {'(': ')', '{': '}', '[': ']', '<': '>'}

    @classmethod
    def get_open_char(cls, c):
        for k, v in cls.open_close_dict.items():
            if c == v:
                return k

    @classmethod
    def is_open(cls, c):
        return c in cls.open_close_dict.keys()

    @classmethod
    def is_close(cls, c):
        return not c in cls.open_close_dict.keys()

    # if valid, returns LINE_IS_VALID
    # if corrupt, returns LINE_IS_CORRUPT, the offending character
    @classmethod
    def check_line(cls, line: str, with_errors=False):
        open_chunks_stack = list()
        for line_c in line:
            if cls.is_open(line_c):
                open_chunks_stack.append(line_c)
            else:
                stack_c = open_chunks_stack.pop()
                if cls.get_open_char(line_c) == stack_c:
                    pass
                else:
                    if (with_errors):
                        print(f"Expected {cls.open_close_dict.get(stack_c)}, but found {line_c}")
                    return cls.LINE_IS_CORRUPTED, line_c

        return cls.LINE_IS_VALID, None

