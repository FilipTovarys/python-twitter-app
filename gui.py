from tkinter import *
from tkinter import filedialog
import main

root = Tk()
root.geometry("")
root.resizable(width=False, height=False)
root.title("Twitter")
root["bg"] = "white"


class App:
    def __init__(self, master):
        self.help_string = None
        self.save_location_text = None
        self.quantity_label = None
        self.v_q = None
        self.progess_label = None
        self.open_file_location = None
        self.v = None
        self.my_font = ("Avenir next", 17)
        self.run_button_graphic = PhotoImage(file="gui/run.png")
        self.second_buttons_graphic = PhotoImage(file="gui/second_buttons.png")
        self.left_frame_graphic = PhotoImage(file="gui/left_frame.png")

        self.frame = Frame(master, bg="white", borderwidth=0)
        self.frame.grid(row=0, column=1, pady=80)
        self.open_file_frame = Frame(self.frame, bg="white", padx=5, pady=5)
        self.open_file_frame.grid()
        self.save_as_frame = Frame(self.frame, bg="white", padx=25, pady=5)
        self.save_as_frame.grid(pady=40)
        self.frame_left = Frame(master, bg="#1DA1F2", height=450, width=450)
        self.frame_left.grid(row=0, column=0, rowspan=2)
        self.left_frame_label = Label(self.frame_left, image=self.left_frame_graphic, border=0)
        self.left_frame_label.grid()

        self.open_file_button = Button(self.open_file_frame, image=self.second_buttons_graphic, borderwidth=0, height=40, width=100, text="Open file", compound=CENTER, fg="#657786", command=self.file_dialog)
        self.open_file_button.grid(row=0, column=0)
        self.run_button = Button(self.frame, bg="white", borderwidth=0, text="Run", font=self.my_font, compound=CENTER, height=60, width=140, image=self.run_button_graphic, command=self.run_and_progress_label)
        self.run_button.grid(pady=35, padx=0)
        self.progess_frame = Frame(master, bg="white", pady=5, padx=5)
        self.progess_frame.grid(row=1, column=1)
        self.open_file_location_status = Label(self.open_file_frame, height=2, width=30, text="File to run", anchor=W, padx=8, bg="white", fg="#657786")
        self.open_file_location_status.grid(row=0, column=1)
        self.save_as_button = Button(self.save_as_frame, command=self.save_dialog, text="Save as", image=self.second_buttons_graphic, borderwidth=0, height=40, width=100, compound=CENTER, fg="#657786")
        self.save_as_button.grid()
        self.save_location = Label(self.save_as_frame, text="Save location", height=2, width=30, anchor=W, padx=8, bg="white", fg="#657786")
        self.save_location.grid(row=0, column=1)
        self.complete = Label(self.progess_frame, text="", bg="white", fg="#657786")
        self.complete.grid(row=0)

    def file_dialog(self):
        self.open_file_location = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if self.open_file_location == "":
            self.open_file_location = None
        else:
            print(f"File adress: {self.open_file_location}")
            self.open_file_location_status["text"] = str(self.open_file_location)
            self.open_file_location_status.grid()
            self.complete["text"] = ""
            self.complete.grid()

    def save_dialog(self):
        self.save_location_text = filedialog.asksaveasfilename()
        self.save_location_text = self.save_location_text + ".txt"
        print(self.save_location_text)
        self.save_location["text"] = self.save_location_text
        self.save_location.grid()

    def run_and_progress_label(self):
        if self.open_file_location is None or self.save_location_text is None:
            print("No file to analyse or no save adress")
        else:
            self.complete["text"] = ""
            self.complete.grid()
            self.help_string = Label(self.progess_frame, text="/", bg="white", fg="#657786")
            self.help_string.grid(row=0, column=1)
            self.v = IntVar()
            self.v_q = IntVar()
            self.progess_label = Label(self.progess_frame, textvariable=self.v, fg="#657786", bg="white")
            self.progess_label.grid(row=0, column=0)
            self.quantity_label = Label(self.progess_frame, textvariable=self.v_q, fg="#657786", bg="white")
            self.quantity_label.grid(row=0, column=2)
            main.main(self.v, root, self.open_file_location, self.v_q, self.save_location_text)
            if self.progess_label["text"] == self.quantity_label["text"]:
                self.progess_label.grid_forget()
                self.quantity_label.grid_forget()
                self.help_string.grid_forget()
                self.complete["text"] = "Complete"
                self.complete.grid()


window = App(root)
root.mainloop()
