###################################
#                                 #
#    Created By DrFrostij         #
#                                 #
###################################


########################
# The imports section  #
########################


import os                       # this is used to get the images + sounds we want                   # (needs pip installment)
# https://docs.python.org/3/library/os.html                                                         #OS documentation
import customtkinter as customtkinter  # this is for the GUI                                        # (needs pip installment)
#https://customtkinter.tomschimansky.com                                                            #Custom Tkinter documentation
import bcrypt                         # this is for the password hashing                            # (needs pip installment)    
#https://www.geeksforgeeks.org/python/hashing-passwords-in-python-with-bcrypt/                      #Bcrypt documentation
from tkinter import messagebox          # this is for small popups                                  # (needs pip installment)
#https://docs.python.org/3/library/tkinter.messagebox.html                                          #Message box documentation    
import tkinter


##############################
# Importing from other files #
##############################


#import # filename          # this is for importing all the varibles from a file

#print(#filename.variable)

##########################
# Main Startup Code Area #
##########################


#Encrypting or checking user data


def encryptionandstorage(username, password):
    print(username, "is the username that has been entered")
    #Hashing
    #https://www.geeksforgeeks.org/python/hashing-passwords-in-python-with-bcrypt/
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    #Textfile writing
    #https://www.geeksforgeeks.org/python/reading-writing-text-files-python/
    with open("DAdatebase.txt", "a+") as file:
        file.seek(0)
        users = file.readlines()
        for user in users:
            stored_username, stored_hash = user.strip().split(":", 1)
            if stored_username == username:
                if bcrypt.checkpw(password.encode("utf-8"), stored_hash.encode("utf-8")):
                    print("Login successful")
                    #Message box
                    #https://docs.python.org/3/library/tkinter.messagebox.html
                    messagebox.showinfo("Login Page", "Login was successful")
                    loginpage.destroy()                               #Deletes the window
                else:
                    print("Login unsuccessful")
                    messagebox.showinfo("Login Page", "Login was unsuccessful")

# Create account GUI

def createaccount():
    global createaccountpage, password, username

    # Window
    createaccountpage = customtkinter.CTk()
    createaccountpage.title("Frost | Create Account")
    createaccountpage.geometry("400x500")
    createaccountpage.resizable(False, False)

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    createaccountpage.configure(fg_color="#10111A")

    # Main container
    frame = customtkinter.CTkFrame(createaccountpage, width=320, height=400, corner_radius=20, fg_color="#191A28")
    frame.place(relx=0.5, rely=0.5, anchor="center")
    frame.grid_columnconfigure(0, weight=1)

    # Title
    title = customtkinter.CTkLabel(frame, text="Create Account", font=("Arial", 30, "bold"), text_color="white")
    title.grid(row=0, column=0, padx=20, pady=(35, 5))

    # Subtitle
    subtitle = customtkinter.CTkLabel(frame, text="Enter your details to create an account", font=("Arial", 13), text_color="#9293A5")
    subtitle.grid(row=1, column=0, pady=(0, 30))

    # Username
    username = customtkinter.CTkEntry(frame, width=260, height=45, corner_radius=10, placeholder_text="Username", fg_color="#242536", border_color="#35364B", text_color="white")
    username.grid(row=2, column=0, padx=25, pady=10)

    # Password
    password = customtkinter.CTkEntry(frame, width=260, height=45, corner_radius=10, placeholder_text="Password", show="*", fg_color="#242536", border_color="#35364B", text_color="white")
    password.grid(row=3, column=0, padx=25, pady=10)

    # Create account button
    createbutton = customtkinter.CTkButton(frame, text="Create Account", width=260, height=45, corner_radius=10, fg_color="#7655D9", hover_color="#6042BB", font=("Arial", 15, "bold"), command=lambda: encryptionandstoragecreateaccount(username.get(), password.get()))
    createbutton.grid(row=4, column=0, padx=25, pady=(25, 10))

    createaccountpage.mainloop()


def encryptionandstoragecreateaccount(username, password):
    print(username, "is the username that has been entered")

    # Check empty fields
    if not username or not password:
        messagebox.showerror("Registration", "Please enter a username and password")
        return

    # Hashing
    # https://www.geeksforgeeks.org/python/hashing-passwords-in-python-with-bcrypt/
    passwordbytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    passwordhash = bcrypt.hashpw(passwordbytes, salt)

    # Textfile writing
    # https://www.geeksforgeeks.org/python/reading-writing-text-files-python/
    with open("DAdatebase.txt", "a") as file:
        file.write(username + ":" + passwordhash.decode('utf-8') + "\n")

    print("User registered")
    messagebox.showinfo("Registration", "You have been successfully registered")
    createaccountpage.destroy()
    loginpage.destroy()



# Login GUI


def loginGUI():
    global loginpage, password, username

    # Window
    loginpage = customtkinter.CTk()
    loginpage.title("Frost | Login")
    loginpage.geometry("400x500")
    loginpage.resizable(False, False)

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    loginpage.configure(fg_color="#10111A")

    # Main container
    frame = customtkinter.CTkFrame(loginpage, width=320, height=400, corner_radius=20, fg_color="#191A28")
    frame.place(relx=0.5, rely=0.5, anchor="center")
    frame.grid_columnconfigure(0, weight=1)

    # Title
    title = customtkinter.CTkLabel(frame, text="Welcome Back", font=("Arial", 30, "bold"), text_color="white")
    title.grid(row=0, column=0, padx=20, pady=(35, 5))

    # Subtitle
    subtitle = customtkinter.CTkLabel(frame, text="Login to access your account", font=("Arial", 13), text_color="#9293A5")
    subtitle.grid(row=1, column=0, pady=(0, 30))

    # Username
    username = customtkinter.CTkEntry(frame, width=260, height=45, corner_radius=10, placeholder_text="Username", fg_color="#242536", border_color="#35364B", text_color="white")
    username.grid(row=2, column=0, padx=25, pady=10)

    # Password
    password = customtkinter.CTkEntry(frame, width=260, height=45, corner_radius=10, placeholder_text="Password", show="*", fg_color="#242536", border_color="#35364B", text_color="white")
    password.grid(row=3, column=0, padx=25, pady=10)

    # Login button
    loginbutton = customtkinter.CTkButton(frame, text="Login", width=260, height=45, corner_radius=10, fg_color="#7655D9", hover_color="#6042BB", font=("Arial", 15, "bold"), command=lambda: encryptionandstorage(username.get(), password.get()))
    loginbutton.grid(row=4, column=0, padx=25, pady=(25, 10))

    # Signup button
    signupbutton = customtkinter.CTkButton(frame, text="Create an account", width=260, height=40, corner_radius=10, fg_color="transparent", hover_color="#29283C", border_width=1, border_color="#7655D9", text_color="#B6A3F5", font=("Arial", 13), command=lambda: createaccount())
    signupbutton.grid(row=5, column=0, padx=25, pady=5)

    # Footer
    cooldesignfooter = customtkinter.CTkLabel(frame, text="Frost | Secure Authentication", font=("Arial", 10), text_color="#68697B")
    cooldesignfooter.grid(row=6, column=0, pady=(25, 15))

    loginpage.mainloop()


loginGUI()

