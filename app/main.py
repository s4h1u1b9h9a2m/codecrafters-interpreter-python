import sys
from enum import Enum

class TokenType(Enum):
    EOF = 0

    # Literals
    IDENTIFIER = 1
    STRING = 2
    NUMBER = 3

    # Single-character tokens
    LEFT_PAREN = "("
    RIGHT_PAREN = ")"
    LEFT_BRACE = "{"
    RIGHT_BRACE = "}"
    COMMA = ","
    DOT = "."
    MINUS = "-"
    PLUS = "+"
    SEMICOLON = ";"
    SLASH = "/"
    STAR = "*"

    # One or two character tokens
    BANG = 15
    BANG_EQUAL = 16
    EQUAL = 17
    EQUAL_EQUAL = 18
    GREATER = 19
    GREATER_EQUAL = 20
    LESS = 21
    LESS_EQUAL = 22

    # Keywords
    AND = 23
    CLASS = 24
    ELSE = 25
    FALSE = 26
    FUN = 27
    FOR = 28
    IF = 29
    NIL = 30
    OR = 31
    PRINT = 32
    RETURN = 33
    SUPER = 34
    THIS = 35
    TRUE = 36
    VAR = 37
    WHILE = 38

class Token:
    def __init__(self, type, lexeme, literal, line):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self):
        if self.literal is not None:
            return f"{self.type.name} {self.lexeme} {self.literal}"
        else:
            return f"{self.type.name} {self.lexeme} null"

    def __repr__(self):
        return self.__str__()

# This function will scan for tokens and return array of tokens
def scan_tokens(content):
    tokens = []
    # token = ""

    for character in content:
        # print(character)
        if character == " " or character == "\r" or character == "\t" or character == "\n":
            # token = ""
            pass
        elif character in [
            TokenType.LEFT_PAREN.value,
            TokenType.RIGHT_PAREN.value,
            TokenType.LEFT_BRACE.value,
            TokenType.RIGHT_BRACE.value,
            TokenType.COMMA.value,
            TokenType.DOT.value,
            TokenType.MINUS.value,
            TokenType.PLUS.value,
            TokenType.SEMICOLON.value,
            TokenType.SLASH.value,
            TokenType.STAR.value
        ]:
            tokens.append(Token(TokenType(character), character, None, 0))
        # elif character == "=" and content[content.index(character) + 1] == "=":
        #     token = "=="
        

    tokens.append(Token(TokenType.EOF, "", None, 0))
    return tokens
    
    # Print <token_type> <lexeme> <literal>
    # for character in content:
    #     print(f"{character} {TokenType.IDENTIFIER}")
    #     if character in ["\n", " "]:
    #         pass
    #     elif character == " ":
    # print("EOF null")

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    # print("Logs from your program will appear here!", file=sys.stderr)

    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()

    # Uncomment this block to pass the first stage
    tokens = []
    if file_contents:
        tokens = scan_tokens(file_contents)
    else:
        print("EOF  null") # Placeholder, remove this line when implementing the scanner

    for token in tokens:
        print(token)


if __name__ == "__main__":
    main()
