# this is the same app as project 8. it is simple with buttons and a combo box
from tkinter import ttk

def open_popup():
    selected_option = combo_box.get()
    popup_message(f"Selected: {selected_option}")

def popup_message(message):
    popup = tk.Toplevel(window)
    popup.title("Pick a car")
    popup_label = tk.Label(popup, text=message, font=('calibre', 14, 'normal'))
    popup_label.pack()

#this is the window - it is to pick a car
window = tk.Tk()
window.title("Car Buyer")


selected_option = tk.StringVar()

#the combo box box for the cars
options = ('No car', 'Seqoia', 'Bongo Skylounge', 'Ford F150')
combo_box = ttk.Combobox(window, width=27, textvariable=selected_option)
combo_box['values'] = options

#this is the button 
button_open_popup = tk.Button(window, text="Choose a Car", font=('calibre', 14, 'normal'), command=open_popup)

#packing everything 
button_open_popup.pack()
combo_box.pack()
combo_box.current(0)


#START THE THING
window.mainloop()