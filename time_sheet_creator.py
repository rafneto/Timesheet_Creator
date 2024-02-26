import customtkinter
import calendar
import datetime
from scrollable_checkbox_frame import ScrollableCheckBoxFrame

year = 0
month = 0

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        global year, month
        
        months = calendar.month_name[1:]
        today = datetime.date.today()
        year = today.year
        month = today.month
        years = [str(x) for x in [year - i for i in range(6)]]
    
        self.title("Time Sheet Creator")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
                
        self.checkbox_frame = customtkinter.CTkFrame(self)
        self.checkbox_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ns")

        optionmenu_month = customtkinter.CTkOptionMenu(self.checkbox_frame, values=months, command=self.optionmenu_month_callback)
        optionmenu_month.set(calendar.month_name[month])
        optionmenu_month.grid(row=0, column=0, padx=15, pady=15, sticky="ns")
        
        optionmenu_year = customtkinter.CTkOptionMenu(self.checkbox_frame, values=years, command=self.optionmenu_year_callback)
        optionmenu_year.set(year)
        optionmenu_year.grid(row=0, column=1, padx=15, pady=15, sticky="ns")

        self.scrollable_checkbox_frame = ScrollableCheckBoxFrame(master=self, width=800, height=600, command=self.label_button_frame_event)
        self.scrollable_checkbox_frame.grid(row=0, column=0, padx=15, pady=15, sticky="ns")
        self.scrollable_checkbox_frame.update_list(calendar.monthrange(year, month)[1])

    def update_frame_by_date(self):
        self.scrollable_checkbox_frame.grid_forget()
        self.scrollable_checkbox_frame.grid(row=1, column=0, padx=15, pady=15, sticky="ns")
        self.scrollable_checkbox_frame.update_list(calendar.monthrange(year, month)[1])

    def optionmenu_month_callback(self, choice):
        global month
        month = datetime.datetime.strptime(choice, '%B').month
        self.update_frame_by_date()
    
    def optionmenu_year_callback(self, choice):
        global year
        year = int(choice)
        self.update_frame_by_date()

    def label_button_frame_event(self, item):
        dummy=0
        #print(f"label button frame clicked: {item}")

if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    app = App()
    app.mainloop()