#NPDA
import graphviz
from IPython.display import display

# Define the states and transitions for NPDA
npda_states = ["q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10", "q11", "q12", "q13", "q14"]
npda_input_alphabet = ["0-9", "UP", "DOWN", "OPEN", "CLOSE", "ENTRY", "EXIT"]
npda_stack_alphabet = ["Z0"]

# Define the transitions for NPDA
npda_transitions = [
    ("q0", "0-9", "Z0", "q1", "Z0"),
    ("q1", "ENTRY", "Z0", "q2", "Z0"),
    ("q2", "UP", "Z0", "q3", "Z0"),
    ("q2", "OPEN", "Z0", "q3", "Z0"),
    ("q2", "CLOSE", "Z0", "q3", "Z0"),
    ("q3", "0-9", "Z0", "q4", "Z0"),
    ("q4", "EXIT", "Z0", "q0", "Z0"),
    ("q0", "0-9", "Z0", "q5", "Z0"),
    ("q5", "ENTRY", "Z0", "q6", "Z0"),
    ("q6", "UP", "Z0", "q7", "Z0"),
    ("q6", "OPEN", "Z0", "q7", "Z0"),
    ("q6", "CLOSE", "Z0", "q7", "Z0"),
    ("q7", "0-9", "Z0", "q8", "Z0"),
    ("q8", "EXIT", "Z0", "q0", "Z0"),
    ("q0", "0-9", "Z0", "q9", "Z0"),
    ("q9", "ENTRY", "Z0", "q10", "Z0"),
    ("q10", "UP", "Z0", "q11", "Z0"),
    ("q10", "OPEN", "Z0", "q11", "Z0"),
    ("q10", "CLOSE", "Z0", "q11", "Z0"),
    ("q11", "0-9", "Z0", "q12", "Z0"),
    ("q12", "EXIT", "Z0", "q0", "Z0"),
    ("q0", "0-9", "Z0", "q13", "Z0"),
    ("q13", "ENTRY", "Z0", "q14", "Z0"),
    ("q14", "UP", "Z0", "q0", "Z0"),
    ("q14", "OPEN", "Z0", "q0", "Z0"),
    ("q14", "CLOSE", "Z0", "q0", "Z0"),
]

# Create a new directed graph for NPDA
npda_dot = graphviz.Digraph(comment="Nondeterministic Pushdown Automaton")

# Add states to the graph
for state in npda_states:
    if state == "q0":
        npda_dot.node(state, state, shape="doublecircle")  # Accepting state
    else:
        npda_dot.node(state, state)

# Add transitions to the graph
for (start, input_symbol, stack_symbol, end, new_stack_symbol) in npda_transitions:
    label = f"{input_symbol}, {stack_symbol} -> {new_stack_symbol}"
    npda_dot.edge(start, end, label=label)

# Display the graph in the notebook
display(npda_dot)
