# FIRST and FOLLOW Computation

from collections import defaultdict

# Grammar Representation
grammar = {
    "E": ["TR"],
    "R": ["+TR", "ε"],
    "T": ["FY"],
    "Y": ["*FY", "ε"],
    "F": ["(E)", "i"]
}

non_terminals = grammar.keys()
terminals = set()

# Identify terminals
for productions in grammar.values():
    for prod in productions:
        for symbol in prod:
            if symbol not in grammar and symbol != "ε":
                terminals.add(symbol)

FIRST = defaultdict(set)
FOLLOW = defaultdict(set)

# Compute FIRST
def compute_first():
    changed = True
    while changed:
        changed = False
        for non_terminal in grammar:
            for production in grammar[non_terminal]:
                for symbol in production:
                    if symbol in terminals:
                        if symbol not in FIRST[non_terminal]:
                            FIRST[non_terminal].add(symbol)
                            changed = True
                        break
                    elif symbol == "ε":
                        if "ε" not in FIRST[non_terminal]:
                            FIRST[non_terminal].add("ε")
                            changed = True
                        break
                    else:
                        before = len(FIRST[non_terminal])
                        FIRST[non_terminal] |= (FIRST[symbol] - {"ε"})
                        if "ε" not in FIRST[symbol]:
                            break
                        if before != len(FIRST[non_terminal]):
                            changed = True

# Compute FOLLOW
def compute_follow():
    start_symbol = list(grammar.keys())[0]
    FOLLOW[start_symbol].add("$")

    changed = True
    while changed:
        changed = False
        for non_terminal in grammar:
            for production in grammar[non_terminal]:
                for i in range(len(production)):
                    symbol = production[i]
                    if symbol in grammar:
                        next_symbols = production[i+1:]
                        temp_first = set()

                        if next_symbols:
                            for s in next_symbols:
                                if s in terminals:
                                    temp_first.add(s)
                                    break
                                else:
                                    temp_first |= (FIRST[s] - {"ε"})
                                    if "ε" not in FIRST[s]:
                                        break
                            else:
                                temp_first.add("ε")
                        else:
                            temp_first.add("ε")

                        before = len(FOLLOW[symbol])
                        FOLLOW[symbol] |= (temp_first - {"ε"})
                        if "ε" in temp_first:
                            FOLLOW[symbol] |= FOLLOW[non_terminal]
                        if before != len(FOLLOW[symbol]):
                            changed = True

compute_first()
compute_follow()

# Print Results
print("\nFIRST Sets:")
for nt in grammar:
    print(f"FIRST({nt}) = {FIRST[nt]}")

print("\nFOLLOW Sets:")
for nt in grammar:
    print(f"FOLLOW({nt}) = {FOLLOW[nt]}")