import customtkinter
import datetime
import pathlib
from scrollable_checkbox_frame import ScrollableCheckBoxFrame
from head_frame import HeadFrame
from freedback_frame import FeedbackFrame
from dialog_error import DialogError
import utils

year = 0
month = 0


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        global year, month
        self.toplevel_window = None
        self.destination_folder = str(pathlib.Path.cwd())
        today = datetime.date.today()
        year = today.year
        month = today.month

        self.title("Time Sheet Creator")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.head_frame = HeadFrame(master=self, fg_color="transparent")
        self.head_frame.grid(row=0, column=0, padx=20, pady=20, sticky="ns")

        self.scrollable_checkbox_frame = ScrollableCheckBoxFrame(
            master=self, width=800, height=400
        )
        self.scrollable_checkbox_frame.grid(
            row=2, column=0, padx=15, pady=5, sticky="ns"
        )
        self.scrollable_checkbox_frame.update_list(
            utils.get_list_of_days_weeks(month, year)
        )

        self.frame = customtkinter.CTkFrame(self)
        self.frame.grid(row=3, column=0, padx=0, pady=0, sticky="ns")

        self.label_directory = customtkinter.CTkLabel(
            self.frame, text=str(pathlib.Path.cwd()), text_color="#8AB5DC", anchor="w"
        )
        self.label_directory.grid(row=0, column=0, padx=15, pady=15, sticky="ns")

        self.button = customtkinter.CTkButton(
            self.frame, text="Change", command=self.change_directory
        )
        self.button.grid(row=0, column=1, padx=15, pady=15, sticky="ns")

        self.feedback_frame = FeedbackFrame(master=self, fg_color="transparent")
        self.feedback_frame.grid(row=4, column=0, padx=0, pady=0, sticky="ns")

        self.button = customtkinter.CTkButton(
            self, text="GENERATE", command=self.button_event
        )
        self.button.grid(row=5, column=0, padx=15, pady=15, sticky="ns")

    def button_event(self):
        list_items = self.scrollable_checkbox_frame.get_checked_list()
        file_name = ""
        try:
            file_name = utils.generate_pdf(
                self.destination_folder, list_items, self.head_frame.get_head_elements()
            )
        except PermissionError:
            message = "File is open in another app"
            self.display_dialog_error(message)
        except Exception as inst:
            message = str(type(inst)) + "\n" + str(inst)
            self.display_dialog_error(message)
        else:
            self.update_feedback_text("File created: " + file_name)

    def update_feedback_text(self, text):
        self.feedback_frame.update(text=text)

    def change_directory(self):
        folder = customtkinter.filedialog.askdirectory(
            initialdir=self.destination_folder
        )
        if folder != "":
            self.destination_folder = folder
            self.label_directory.configure(text=folder)

    def display_dialog_error(self, message):
        print(message)
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = DialogError(
                self
            )  # create window if its None or destroyed
            self.toplevel_window.setText(message)
            self.toplevel_window.focus()
        else:
            self.toplevel_window.focus()  # if window exists focus it


if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    app = App()
    app.after(201, lambda: app.iconbitmap(".\\icon.ico"))
    app.mainloop()
