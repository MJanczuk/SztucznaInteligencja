import tkinter as tk
from tkinter import ttk

# Tworzenie okna głównego
root = tk.Tk()
root.title("Treeview Example")

# Tworzenie widżetu ttk.Treeview
tree = ttk.Treeview(root, columns=("Name", "Age", "City"))

# Definiowanie nagłówków kolumn
tree.heading("#1", text="Name")
tree.heading("#2", text="Age")
tree.heading("#3", text="City")

# Dodawanie wierszy do widżetu
tree.insert("", "end", iid=2, values=("John Doe", 30, "New York"))
tree.insert("", "end", values=("Jane Smith", 25, "Los Angeles"))
tree.insert("", "end", values=("Bob Johnson", 40, "Chicago"))

# Wyświetlenie widżetu na ekranie
tree.pack()

root.mainloop()
