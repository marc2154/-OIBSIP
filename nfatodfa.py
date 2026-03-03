# NFA to DFA Conversion using Subset Construction

from collections import defaultdict, deque

# Define NFA
nfa = {
    'q0': {'a': ['q0', 'q1'], 'b': ['q0']},
    'q1': {'a': ['q2'], 'b': []},
    'q2': {'a': [], 'b': []}
}

states = ['q0', 'q1', 'q2']
alphabet = ['a', 'b']
start_state = 'q0'
final_states = ['q2']


def nfa_to_dfa(nfa, start_state, final_states, alphabet):
    dfa = {}
    queue = deque()
    start = frozenset([start_state])
    queue.append(start)
    dfa_states = {start}
    
    while queue:
        current = queue.popleft()
        dfa[current] = {}
        
        for symbol in alphabet:
            next_state = set()
            
            for state in current:
                if symbol in nfa[state]:
                    next_state.update(nfa[state][symbol])
            
            next_state = frozenset(next_state)
            dfa[current][symbol] = next_state
            
            if next_state not in dfa_states:
                dfa_states.add(next_state)
                queue.append(next_state)
    
    return dfa


dfa = nfa_to_dfa(nfa, start_state, final_states, alphabet)

print("\nDFA Transition Table:\n")

for state in dfa:
    print(f"{set(state)}")
    for symbol in alphabet:
        print(f"  --{symbol}--> {set(dfa[state][symbol])}")
    print()

# Identify DFA Final States
print("DFA Final States:")
for state in dfa:
    if any(s in final_states for s in state):
        print(set(state))