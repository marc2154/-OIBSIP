# Grammar Transformation Tool
# Performs:
# 1. Left Recursion Elimination
# 2. Left Factoring

from collections import defaultdict

# -------- INPUT GRAMMAR --------
grammar = {
    "E": ["E+T", "T"],
    "S": ["ifEthenSelseS", "ifEthenS"]
}

# --------------------------------


def eliminate_left_recursion(grammar):
    new_grammar = {}

    for non_terminal in grammar:
        productions = grammar[non_terminal]
        alpha = []
        beta = []

        for prod in productions:
            if prod.startswith(non_terminal):
                alpha.append(prod[len(non_terminal):])
            else:
                beta.append(prod)

        if alpha:
            new_non_terminal = non_terminal + "'"
            new_grammar[non_terminal] = [b + new_non_terminal for b in beta]
            new_grammar[new_non_terminal] = [a + new_non_terminal for a in alpha]
            new_grammar[new_non_terminal].append("ε")
        else:
            new_grammar[non_terminal] = productions

    return new_grammar


def left_factoring(grammar):
    factored_grammar = {}

    for non_terminal in grammar:
        productions = grammar[non_terminal]
        prefix_dict = defaultdict(list)

        for prod in productions:
            prefix_dict[prod[0]].append(prod)

        if any(len(v) > 1 for v in prefix_dict.values()):
            new_non_terminal = non_terminal + "F"
            factored_grammar[non_terminal] = []
            factored_grammar[new_non_terminal] = []

            for key in prefix_dict:
                group = prefix_dict[key]
                if len(group) > 1:
                    factored_grammar[non_terminal].append(key + new_non_terminal)
                    for prod in group:
                        factored_grammar[new_non_terminal].append(prod[1:] or "ε")
                else:
                    factored_grammar[non_terminal].append(group[0])
        else:
            factored_grammar[non_terminal] = productions

    return factored_grammar


def print_grammar(grammar, title):
    print("\n" + title)
    print("-" * len(title))
    for non_terminal in grammar:
        print(f"{non_terminal} -> {' | '.join(grammar[non_terminal])}")


# -------- EXECUTION --------

print_grammar(grammar, "Original Grammar")

grammar_no_lr = eliminate_left_recursion(grammar)
print_grammar(grammar_no_lr, "After Eliminating Left Recursion")

grammar_factored = left_factoring(grammar_no_lr)
print_grammar(grammar_factored, "After Left Factoring")