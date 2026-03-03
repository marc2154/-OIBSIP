

from collections import defaultdict

grammar = {
    "E": ["TR"],
    "R": ["+TR", "ε"],
    "T": ["FY"],
    "Y": ["*FY", "ε"],
    "F": ["(E)", "i"]
}

FIRST = {
    "E": {"(", "i"},
    "R": {"+", "ε"},
    "T": {"(", "i"},
    "Y": {"*", "ε"},
    "F": {"(", "i"}
}

FOLLOW = {
    "E": {")", "$"},
    "R": {")", "$"},
    "T": {"+", ")", "$"},
    "Y": {"+", ")", "$"},
    "F": {"*", "+", ")", "$"}
}

parsing_table = defaultdict(dict)


for non_terminal in grammar:
    for production in grammar[non_terminal]:
        first_set = set()

        for symbol in production:
            if symbol in FIRST:
                first_set |= (FIRST[symbol] - {"ε"})
                if "ε" not in FIRST[symbol]:
                    break
            else:
                first_set.add(symbol)
                break
        else:
            first_set.add("ε")


        for terminal in first_set - {"ε"}:
            parsing_table[non_terminal][terminal] = production

        if "ε" in first_set:
            for terminal in FOLLOW[non_terminal]:
                parsing_table[non_terminal][terminal] = production


print("\nPredictive Parsing Table:\n")

for nt in parsing_table:
    for t in parsing_table[nt]:
        print(f"M[{nt}][{t}] = {nt} → {parsing_table[nt][t]}")