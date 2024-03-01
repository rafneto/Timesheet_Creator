import customtkinter


class ScrollableCheckBoxFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.command = command

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=2)
        self.grid_columnconfigure(3, weight=2)
        self.grid_columnconfigure(4, weight=4)

        self.build_table_head()

    def build_table_head(self):
        self.checkbox_list = []
        count = 0
        for title in ["DAY", "DAYWEEK", "1st. Period", "2nd. Period"]:
            label = customtkinter.CTkLabel(
                self, text=title, compound="left", padx=15, anchor="w"
            )
            label.grid(row=0, column=count, padx=(10, 10), pady=(10, 10))
            self.checkbox_list.append(label)
            count = count + 1

    def add_item(self, item):
        label_num = customtkinter.CTkLabel(
            self, text=item[0], compound="left", anchor="w"
        )
        label_name = customtkinter.CTkLabel(
            self, text=item[1], compound="left", padx=15, anchor="w"
        )
        entry = customtkinter.CTkEntry(self, placeholder_text="Observations", width=200)
        checkbox = customtkinter.CTkCheckBox(self, text="9:00 - 13:00")
        checkbox2 = customtkinter.CTkCheckBox(self, text="14:00 - 18:00")

        if self.command is not None:
            checkbox.configure(command=self.command(item[0]))
            checkbox2.configure(command=self.command(item[0]))

        label_num.grid(
            row=len(self.checkbox_list), column=0, padx=(10, 10), pady=(10, 10)
        )
        label_name.grid(
            row=len(self.checkbox_list), column=1, padx=(10, 10), pady=(10, 10)
        )
        checkbox.grid(
            row=len(self.checkbox_list), column=2, padx=(10, 10), pady=(10, 10)
        )
        checkbox2.grid(
            row=len(self.checkbox_list), column=3, padx=(10, 10), pady=(10, 10)
        )
        checkbox.select()
        checkbox2.select()
        entry.grid(row=len(self.checkbox_list), column=4, padx=(10, 10), pady=(10, 10))

        if item[1] == "Sunday" or item[1] == "Saturday":
            label_num.configure(state="disabled")
            label_name.configure(state="disabled")
            checkbox.deselect()
            checkbox2.deselect()
            checkbox.configure(state="disabled")
            checkbox2.configure(state="disabled")
            entry.insert(0, "Weekend")
            entry.configure(state="disabled")

        save_row = (label_num, checkbox, checkbox2, entry)
        self.checkbox_list.append(save_row)

    def update_list(self, items):
        self.build_table_head()
        for i in items:
            self.add_item(i)

    def get_checked_list(self):
        count = 0
        list_items = []
        for item in self.checkbox_list:
            if count > 3:
                (label_num, checkbox, checkbox2, entry) = item
                obs = entry.get()
                isWeekend = False
                if obs == "":
                    obs = "---"
                elif obs == "Weekend":
                    isWeekend = True
                dict_items = {
                    "day": str(label_num.cget("text")),
                    "checkbox": checkbox.get(),
                    "checkbox2": checkbox2.get(),
                    "obs": obs,
                    "isWeekend": isWeekend,
                }
                list_items.append(dict_items)
            count = count + 1
        return list_items
