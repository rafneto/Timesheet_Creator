import customtkinter
from time import sleep
from threading import Thread

NUM_SEC=3

class FeedbackFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.switch_var = customtkinter.StringVar(value="pt")
        switch = customtkinter.CTkSwitch(self, text="PDF in PT-pt", 
                                         command=self.switch_event,variable=self.switch_var, onvalue="pt", offvalue="en")
        switch.grid(row=0, column=0, padx=0, pady=0, sticky="ns")
        
        self.label_feedback = customtkinter.CTkLabel(self, text="",text_color="#7fb785", anchor="w")
        self.label_feedback.grid(row=1, column=0, padx=0, pady=0, sticky="ns")
        
    def update(self, text):
        self.label_feedback.configure(text=text)
        thread = AsyncUpdater(self.label_feedback)
        thread.start()
        
    def switch_event(self):
        #TODO: implement translation switch
        print("switch toggled, current value:", self.switch_var.get())
        
class AsyncUpdater(Thread):
    def __init__(self, label):
        super().__init__()
        self.label=label

    def run(self):
        sleep(NUM_SEC)
        self.label.configure(text='')