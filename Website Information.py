import socket
from ip2geotools.databases.noncommercial import DbIpCity
from tkinter import *
from tkinter import messagebox

def get_information():
    if not url_entrybox.get():
        messagebox.showerror("Error", "Please enter a website name or IP address!!")
        return
    if information_label.get("1.0", END):
        information_label.delete("1.0", END)
    info = url_entrybox.get()
    try:
        response = DbIpCity.get(info)
    except:
        ip = socket.gethostbyname(info)
        response = DbIpCity.get(ip)
        
    information_label.insert(END, f"IP:{response.ip_address}\nCity:{response.city}\nRegion:{response.region}\nCountry:{response.country}")
    url_entrybox.delete(0,END)
    
root = Tk()
root.title("IP info")
root.configure(bg = "orange")

enter_url_label = Label(root, text = "Enter the url(Or IP):", font = ("Verdana", 15), bg = "orange")
enter_url_label.grid(row = 0, column = 0, pady = 10, sticky = W)

url_entrybox = Entry(root, width = 50, font = ("Comic Sans MS", 15))
url_entrybox.grid(row = 0, column = 1, sticky = W)

get_info_button = Button(root, text = "Get info", font = ("Verdana", 10), command = get_information)
get_info_button.grid(row = 1, column = 1, sticky = W)

info_label = Label(root, text = "Information:", font = ("Verdana", 30), bg = "orange")
info_label.grid(row = 2, column = 0, pady = 10, sticky = W)

information_label = Text(root, height = 5, width = 30, font = ("Times New Roman", 20), relief = SUNKEN)
information_label.grid(row = 3, column = 0, pady = 10)

root.mainloop()
