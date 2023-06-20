import tkinter as tk

def calculate_new_steps_per_mm():
    steps_per_mm = float(steps_per_mm_entry.get())
    extruded_distance = float(extruded_distance_entry.get())

    X = steps_per_mm * 100
    new_steps_per_mm = X / extruded_distance

    new_steps_per_mm_label.config(text="New steps/mm value: {:.2f}".format(new_steps_per_mm))

root = tk.Tk()
root.title("Extruder Calibration Calculator")

steps_per_mm_label = tk.Label(root, text="Enter steps/mm:")
steps_per_mm_label.pack()

steps_per_mm_entry = tk.Entry(root)
steps_per_mm_entry.pack()

extruded_distance_label = tk.Label(root, text="Enter extruded distance (mm):")
extruded_distance_label.pack()

extruded_distance_entry = tk.Entry(root)
extruded_distance_entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_new_steps_per_mm)
calculate_button.pack()

new_steps_per_mm_label = tk.Label(root, text="")
new_steps_per_mm_label.pack()

root.mainloop()
