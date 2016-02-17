import re


class KeyWords:
    CLASS = 1
    METHOD = 2
    FUNCTION = 3
    CONSTRUCTOR = 4
    INT = 5
    BOOLEAN = 6
    CHAR = 7
    VOID = 8
    VAR = 9
    STATIC = 10
    FIELD = 11
    LET = 12
    DO = 13
    IF = 14
    ELSE = 15
    WHILE = 16
    RETURN = 17
    TRUE = 18
    FALSE = 19
    NULL = 20
    THIS = 21

class Symbols:
    LEFT_CURLY_BRACKET = 22
    RIGHT_CURLY_BRACKET = 23
    LEFT_ROUND_BRACKET = 24
    RIGHT_ROUND_BRACKET = 25
    LEFT_BOX_BRACKET = 26
    RIGHT_BOX_BRACKET = 27
    DOT = 25
    COMMA = 26
    SEMI_COLON = 27
    PLUS = 28
    MINUS = 29
    MULTI = 30
    DIV = 31
    AND = 32
    PIPE = 33
    LESS_THAN = 34
    GREATER_THAN = 35
    EQUAL = 36
    TILDE = 37
    ASTERISK = 38

class Constants:

    class TokenType:
        SYMBOL = 1
        IDENTIFIER = 2
        INT_CONST = 3
        STRING_CONST = 4
        KEYWORD = 5
        COMMENT_START = 6
        COMMENT_END = 6

    class Tokens:
        KEYWORDS = {
            'class': KeyWords.CLASS,
            'constructor': KeyWords.CONSTRUCTOR,
            'function': KeyWords.FUNCTION,
            'method': KeyWords.METHOD,
            'field': KeyWords.FIELD,
            'static': KeyWords.STATIC,
            'var': KeyWords.VAR,
            'int': KeyWords.INT,
            'char': KeyWords.CHAR,
            'boolean': KeyWords.BOOLEAN,
            'void': KeyWords.VOID,
            'true': KeyWords.TRUE,
            'false': KeyWords.FALSE,
            'null': KeyWords.NULL,
            'this': KeyWords.THIS,
            'let': KeyWords.LET,
            'do': KeyWords.DO,
            'if': KeyWords.IF,
            'else': KeyWords.ELSE,
            'while': KeyWords.WHILE,
            'return': KeyWords.RETURN
        }

        SYMBOLS = [
            '{',
            '}',
            '(',
            ')',
            '[',
            ']',
            '.',
            ',',
            ';',
            '+',
            '-',
            '*',
            '/',
            '&',
            '|',
            '<',
            '>',
            '=',
            '~'
        ]

        LINE_COMMENT_START = '//'

        COMMENT_START = '/*'

        COMMENT_END = '*/'

        IDENTIFIER_PATTERN = re.compile(r'^[A-Za-z_][A-Za-z0-9_]*$')

        INTEGER_PATTERN = re.compile(r'^[0-9]+$')

        STRING_PATTERN = re.compile(r'^".*"$')

class TokenType:
    SYMBOL = 1
    IDENTIFIER = 2
    INT_CONST = 3
    STRING_CONST = 4
    KEYWORD = 5
    COMMENT_START = 6
    COMMENT_END = 6

class Token:
    def __init__(self):
        pass

class Tokens:
    KEYWORDS = {
        'class': KeyWords.CLASS,
        'constructor': KeyWords.CONSTRUCTOR,
        'function': KeyWords.FUNCTION,
        'method': KeyWords.METHOD,
        'field': KeyWords.FIELD,
        'static': KeyWords.STATIC,
        'var': KeyWords.VAR,
        'int': KeyWords.INT,
        'char': KeyWords.CHAR,
        'boolean': KeyWords.BOOLEAN,
        'void': KeyWords.VOID,
        'true': KeyWords.TRUE,
        'false': KeyWords.FALSE,
        'null': KeyWords.NULL,
        'this': KeyWords.THIS,
        'let': KeyWords.LET,
        'do': KeyWords.DO,
        'if': KeyWords.IF,
        'else': KeyWords.ELSE,
        'while': KeyWords.WHILE,
        'return': KeyWords.RETURN
    }

    SYMBOLS = {
        '{': Symbols.LEFT_CURLY_BRACKET,
        '}': Symbols.RIGHT_CURLY_BRACKET,
        '(': Symbols.LEFT_ROUND_BRACKET,
        ')': Symbols.RIGHT_ROUND_BRACKET,
        '[': Symbols.LEFT_BOX_BRACKET,
        ']': Symbols.RIGHT_BOX_BRACKET,
        '.': Symbols.DOT,
        ',': Symbols.COMMA,
        ';': Symbols.SEMI_COLON,
        '+': Symbols.PLUS,
        '-': Symbols.MINUS,
        '*': Symbols.ASTERISK,
        '/': Symbols.DIV,
        '&': Symbols.AND,
        '|': Symbols.PIPE,
        '<': Symbols.LESS_THAN,
        '>': Symbols.GREATER_THAN,
        '=': Symbols.EQUAL,
        '~': Symbols.TILDE
    }

    LINE_COMMENT_START = '//'

    COMMENT_START = '/*'

    COMMENT_END = '*/'

    IDENTIFIER_PATTERN = re.compile(r'^[A-Za-z_][A-Za-z0-9_]*$')

    INTEGER_PATTERN = re.compile(r'^[0-9]+$')

    STRING_PATTERN = re.compile(r'^".*"$')
