import customtkinter
import calendar
import datetime
import utils

year = 0
month = 0

class HeadFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master=master
        global year, month
        
        self.grid_columnconfigure(0, weight=4)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=3)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        months=calendar.month_name[1:]
        today=datetime.date.today()
        year=today.year
        month=today.month
        years=[str(x) for x in [year - i for i in range(6)]]
                
        self.entry_employer=customtkinter.CTkEntry(self, placeholder_text="Employer", width=400)
        self.entry_employer.grid(row=0, column=0, padx=15, pady=15, sticky="ns")
        
        self.entry_headoffice=customtkinter.CTkEntry(self, placeholder_text="Head Office")
        self.entry_headoffice.grid(row=0, column=1, padx=15, pady=15, sticky="ns")
        
        self.entry_localoffice=customtkinter.CTkEntry(self, placeholder_text="Local Office")
        self.entry_localoffice.grid(row=0, column=2, padx=15, pady=15, sticky="ns") 
        
        self.entry_employee=customtkinter.CTkEntry(self, placeholder_text="Name Employee", width=400)
        self.entry_employee.grid(row=1, column=0, padx=15, pady=15, sticky="ns")
        
        self.optionmenu_month=customtkinter.CTkOptionMenu(self, values=months, command=self.optionmenu_month_callback)
        self.optionmenu_month.set(calendar.month_name[month])
        self.optionmenu_month.grid(row=1, column=1, padx=15, pady=15, sticky="ns")
        
        self.optionmenu_year=customtkinter.CTkOptionMenu(self, values=years, command=self.optionmenu_year_callback)
        self.optionmenu_year.set(year)
        self.optionmenu_year.grid(row=1, column=2, padx=15, pady=15, sticky="ns")
        
    def optionmenu_month_callback(self, choice):
        global month
        month=datetime.datetime.strptime(choice, '%B').month
        self.update_frame_by_date()
    
    def optionmenu_year_callback(self, choice):
        global year
        year=int(choice)
        self.update_frame_by_date()
        
    def update_frame_by_date(self):
        for widget in self.master.scrollable_checkbox_frame.winfo_children():
            widget.destroy()
        self.master.scrollable_checkbox_frame.grid(row=1, column=0, padx=15, pady=15, sticky="ns")
        self.master.scrollable_checkbox_frame.update_list(utils.get_list_of_days_weeks(month, year))
        
    def get_head_elements(self):
        headers={
            "name": self.entry_employee.get(),
            "company": self.entry_employer.get(),
            "headoffice": self.entry_localoffice.get(),
            "localoffice": self.entry_localoffice.get(),
            "month": calendar.month_name[month],
            "year": str(year)
            }
        return headers