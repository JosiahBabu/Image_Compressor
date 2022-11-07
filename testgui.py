"""import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def browseFile():
    filename=filedialog.askdirectory(initialdir="/",

                                        title="Select the destination",
                                        )
    message.configure(text="Selected Folder"+filename)
root = tk.Tk()

# place a label on the root window
root.title('Size Reducer')
root.geometry('600x400+50+50')
root.resizable(0, 0)
root.attributes('-topmost', 1)
root.iconbitmap('icon123.ico')

message = tk.Label(root, text="Hello, World!")
message.pack()
ttk.Label(root, text='Themed Label').pack()
utton = ttk.Button(root, text="Choose Folder", command=browseFile).pack(ipadx=5,ipady=5,expand=True)
# keep the window dis
"""
import tkinter as tk
from tkinter import TclError, ttk,StringVar
from tkinter import filedialog
import Image_reducer_test as irt

Source_Path="Select source path"
Output_path="Select Output path"

def browseFile():
    filename=filedialog.askdirectory(initialdir="/",title="Select the destination")
    Source_Path=filename
    keyword.delete(0,tk.END)
    keyword.insert(0,Source_Path)
def browseFileOut():
    filename=filedialog.askdirectory(initialdir="/",title="Select the output destination")
    Output_path=filename
    replacement.delete(0,tk.END)
    replacement.insert(0,Output_path)


def update_list_box_gui():
    print("finished")
    return listbox


def update_lbl(val):
   manual['text'] = "Scale at " + val


def run_script():
    irt.main()


def create_input_frame(container):

    frame = ttk.Frame(container)

    # grid layout for the input frame
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=3)

    ttk.Label(frame, text='Source Folder:').grid(column=0, row=0, sticky=tk.W)
    global keyword
    keyword = ttk.Entry(frame, width=30)
    keyword.focus()
    keyword.grid(column=1, row=0, sticky=tk.W)


    ttk.Label(frame, text='Destination Folder:').grid(column=0, row=1, sticky=tk.W)
    global replacement
    replacement = ttk.Entry(frame, width=30)
    replacement.focus()
    replacement.grid(column=1, row=1, sticky=tk.W)

    for widget in frame.winfo_children():
        widget.grid(padx=3, pady=3)

    return frame


def create_button_frame(container):
    frame = ttk.Frame(container)

    frame.columnconfigure(0, weight=1)

    ttk.Button(frame, text='Choose Folder',command=browseFile).grid(column=0, row=1)
    ttk.Button(frame, text='Choose Folder',command=browseFileOut).grid(column=0, row=2)


    for widget in frame.winfo_children():
        widget.grid(padx=3, pady=3)

    return frame



def create_submit_button(container):

    frame = ttk.Frame(container)
    frame.columnconfigure(0, weight=1)
    ttk.Button(frame, text='Submit',command=run_script).grid(column=0, row=1)
    for widget in frame.winfo_children():
        widget.grid(padx=3, pady=3)

    return frame


def create_list_box(container):
    frame=ttk.Frame(container)
    frame.columnconfigure(0,weight=1)
    global listbox
    listbox = tk.Listbox(frame,height=6,selectmode=tk.EXTENDED)
    for widget in frame.winfo_children():
        widget.grid(padx=3, pady=3)
    return frame



def create_scale_quality(container):

    frame=ttk.Frame(container)
    frame.columnconfigure(0,weight=1)
    num = StringVar()
    ttk.Label(frame,text="quality").grid(column=0,row=0,sticky='we')
    ttk.Label(frame, textvariable=num).grid(column=1, row=0, sticky='we')
    manual = ttk.Label(frame)
    manual.grid(column=0, row=1, sticky='we')
    scale = ttk.Scale(frame, orient='horizontal', length=100, from_=1, to=100,variable=num,)
    for widget in frame.winfo_children():
        widget.grid(padx=3, pady=3)
    return frame


def create_main_window():
    root = tk.Tk()
    root.title('Size Reducer')
    root.resizable(0, 0)
    try:
        # windows only (remove the minimize/maximize button)
        root.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')

    # layout on the root window
    root.columnconfigure(0, weight=4)
    root.columnconfigure(1, weight=1)


    input_frame = create_input_frame(root)
    input_frame.grid(column=0, row=0)

    button_frame = create_button_frame(root)
    button_frame.grid(column=1, row=0)

    submit_button_frame = create_submit_button(root)
    submit_button_frame.grid(column=1, row=2)

    scale_view = create_scale_quality(root)
    scale_view.grid(column=0, row=3)


    listbox_view = create_list_box(root)
    listbox_view.grid(column=0, row=4)

    root.mainloop()


if __name__ == "__main__":

    create_main_window()
