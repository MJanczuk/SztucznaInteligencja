import tkinter as tk
from tkinter import scrolledtext
from graphviz import Digraph

def generate_uml_action_diagram():
    dot = Digraph(comment='UML Action Diagram', format='png')
    dot.node('Start', 'Start')
    dot.node('Action1', 'Action 1')
    dot.node('Action2', 'Action 2')
    dot.node('End', 'End')
    dot.edge('Start', 'Action1')
    dot.edge('Action1', 'Action2')
    dot.edge('Action2', 'End')
    dot.render('uml_action_diagram', view=True)

def display_uml_action_diagram():
    generate_uml_action_diagram()
    text.delete(1.0, tk.END)
    text.insert(tk.END, "UML Action Diagram generated and displayed.")

root = tk.Tk()
root.title("Prosty GUI z grafem UML Akcji")

frame = tk.Frame(root)
frame.pack()

generate_button = tk.Button(frame, text="Generate UML Action Diagram", command=display_uml_action_diagram)
generate_button.pack()

text = scrolledtext.ScrolledText(frame, width=40, height=10)
text.pack()

root.mainloop()