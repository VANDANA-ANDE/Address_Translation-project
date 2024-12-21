# gui.py
from tkinter import *
from simulation import simulate_address_translation

def simulate_translation():
    virtual_address = int(virtual_address_entry.get())
    physical_address, status, access_time = simulate_address_translation(
        virtual_address, 4096, {}, {0: 5, 1: 7, 2: 3}
    )
    if physical_address != -1:
        result_label.config(
            text=f"Physical Address: {physical_address}\nStatus: {status}\nAccess Time: {access_time}ns"
        )
    else:
        result_label.config(
            text=f"Status: {status}\nPage Fault | Access Time: {access_time}ns"
        )

root = Tk()
root.title("Address Translation Simulation")

# GUI Widgets
Label(root, text="Virtual Address:").grid(row=0, column=0)
virtual_address_entry = Entry(root)
virtual_address_entry.grid(row=0, column=1)
Button(root, text="Simulate", command=simulate_translation).grid(row=1, column=0, columnspan=2)
result_label = Label(root, text="Result will appear here")
result_label.grid(row=2, column=0, columnspan=2)

root.mainloop()
