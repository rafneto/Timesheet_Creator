import customtkinter

class ScrollableCheckBoxFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.command = command
        self.checkbox_list = []
        
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=2)
        self.grid_columnconfigure(3, weight=4)

    def add_item(self, item):
        label = customtkinter.CTkLabel(self, text=item, compound="left", padx=15, anchor="w")
        entry = customtkinter.CTkEntry(self, placeholder_text="Observações", width=200)
        checkbox = customtkinter.CTkCheckBox(self, text="9:00 - 13:00")
        checkbox2 = customtkinter.CTkCheckBox(self, text="14:00 - 18:00")

        if self.command is not None:
            checkbox.configure(command=self.command(item))
            checkbox2.configure(command=self.command(item))

        label.grid(row=len(self.checkbox_list), column=0, padx=(10, 10), pady=(10, 10))
        checkbox.grid(row=len(self.checkbox_list), column=1, padx=(10, 10), pady=(10, 10))
        checkbox2.grid(row=len(self.checkbox_list), column=2, padx=(10, 10), pady=(10, 10))
        entry.grid(row=len(self.checkbox_list), column=3, padx=(10, 10), pady=(10, 10))

        self.checkbox_list.append(label)
        self.checkbox_list.append(checkbox)
        self.checkbox_list.append(checkbox2)
        self.checkbox_list.append(entry)

    def update_list(self, size):
        for i in range(1, size + 1):
            self.add_item(f"Day {i}")
    