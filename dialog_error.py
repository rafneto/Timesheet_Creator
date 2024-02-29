import customtkinter

class DialogError(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("300x100")
        self.title("ERRO")
    
    def setText(self, msg):
        self.label = customtkinter.CTkLabel(self, text=msg)
        self.label.pack(padx=20, pady=20)
        