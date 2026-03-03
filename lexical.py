

import re
keywords = {
    "int", "float", "if", "else", "while", "for",
    "return", "break", "continue", "char", "double", "void"
}
operators = {
    "+", "-", "*", "/", "=", "==", "!=", "<", ">", "<=", ">="
}
delimiters = {"(", ")", "{", "}", "[", "]", ",", ";"}

def lexical_analyzer(code):
    tokens = []
    pattern = r'\".*?\"|\w+|==|!=|<=|>=|[+\-*/=<>;,(){}\[\]]'
    words = re.findall(pattern, code)
    
    for word in words:
        if word in keywords:
            tokens.append(("KEYWORD", word))
        elif word in operators:
            tokens.append(("OPERATOR", word))
        elif word in delimiters:
            tokens.append(("DELIMITER", word))
        elif word.isdigit():
            tokens.append(("NUMBER", word))
        elif word.startswith('"') and word.endswith('"'):
            tokens.append(("STRING", word))
        elif word.isidentifier():
            tokens.append(("IDENTIFIER", word))
        else:
            tokens.append(("UNKNOWN", word))
    
    return tokens
code = """
int main() {
    int a = 10;
    float b = 20;
    if(a < b) {
        return a;
    }
}
"""
result = lexical_analyzer(code)
print("TOKENS:\n")
for token in result:
    print(token)