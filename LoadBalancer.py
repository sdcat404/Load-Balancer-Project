import customtkinter
import requests
import threading
#-----------------------Pretty things----------------------#
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()
root.geometry("500x350")
root.title("Iron Load Balancer")
#-----------------------Pretty things----------------------#

#-----------------------Load Function----------------------#

def load():
    for _ in range(2):
        while True:
                request = requests.get
                request (entry.get())
                x = threading.Thread(target=load)
                x.start()
                print ('requests: ', threading.active_count())
#-----------------------Load Function----------------------#



frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

lable = customtkinter.CTkLabel(master=frame, text="edit me", text_font=("Roboto", 24))
lable.pack(pady=12, padx=10)

entry = customtkinter.CTkEntry(master=frame, placeholder_text="Host Name / IP Address")
entry.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Start",text_font=("Roboto", 15), command=load)
button.pack(pady=12, padx=10)

root.mainloop()
