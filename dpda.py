#DPDA
import graphviz
from IPython.display import display

# Define the states and transitions for DPDA
dpda_states = ["q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10", "q11", "q12", "q13", "q14"]
dpda_input_alphabet = ["0-9", "UP", "DOWN", "OPEN", "CLOSE", "ENTRY", "EXIT"]
dpda_stack_alphabet = ["Z0"]

# Define the transitions for DPDA
dpda_transitions = [
    ("q0", "0-9", "Z0", "q1", "Z0"),
    ("q1", "ENTRY", "Z0", "q2", "Z0"),
    ("q2", "UP", "Z0", "q3", "Z0"),  # Ensuring determinism with only one transition for each input
    ("q3", "0-9", "Z0", "q4", "Z0"),
    ("q4", "EXIT", "Z0", "q0", "Z0"),
    ("q0", "0-9", "Z0", "q5", "Z0"),
    ("q5", "ENTRY", "Z0", "q6", "Z0"),
    ("q6", "OPEN", "Z0", "q7", "Z0"),  # Ensuring determinism with only one transition for each input
    ("q7", "0-9", "Z0", "q8", "Z0"),
    ("q8", "EXIT", "Z0", "q0", "Z0"),
    ("q0", "0-9", "Z0", "q9", "Z0"),
    ("q9", "ENTRY", "Z0", "q10", "Z0"),
    ("q10", "CLOSE", "Z0", "q11", "Z0"),  # Ensuring determinism with only one transition for each input
    ("q11", "0-9", "Z0", "q12", "Z0"),
    ("q12", "EXIT", "Z0", "q0", "Z0"),
    ("q0", "0-9", "Z0", "q13", "Z0"),
    ("q13", "ENTRY", "Z0", "q14", "Z0"),
    ("q14", "UP", "Z0", "q0", "Z0"),  # Ensuring determinism with only one transition for each input
]

# Create a new directed graph for DPDA
dpda_dot = graphviz.Digraph(comment="Deterministic Pushdown Automaton")

# Add states to the graph
for state in dpda_states:
    if state == "q0":
        dpda_dot.node(state, state, shape="doublecircle")  # Accepting state
    else:
        dpda_dot.node(state, state)

# Add transitions to the graph
for (start, input_symbol, stack_symbol, end, new_stack_symbol) in dpda_transitions:
    label = f"{input_symbol}, {stack_symbol} -> {new_stack_symbol}"
    dpda_dot.edge(start, end, label=label)

# Display the graph in the notebook
display(dpda_dot)

