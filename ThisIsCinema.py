import tkinter as tk
from tkinter import ttk
import webbrowser
from PIL import Image, ImageTk


a = tk.Tk()
a.title("This is Cinema!!")
a.geometry("500x550")
a.configure(bg='#222222')


# logo 
logo_image = Image.open("C:\\Users\\ELCOT\\Desktop\\Project ThisIsCinema\\Templates\\ThisIsCinima.jfif")
logo_image = logo_image.resize((350,250))
logo = ImageTk.PhotoImage(logo_image)


logo_label = tk.Label(a, image=logo, bg='#222222')
logo_label.image = logo  
logo_label.pack(side="top", pady=20)


def username():
    global username_entry
#  username label and password label
username_label = ttk.Label(a, text="Username:", font=("Helvetica", 12), foreground="white", background="#222222")
username_label.pack(pady=10)

username_entry = ttk.Entry(a, font=("Helvetica", 12), width=30)
username_entry.pack()


password_label = ttk.Label(a, text="Password:", font=("Helvetica", 12), foreground="white", background="#222222")
password_label.pack(pady=10)

password_entry = ttk.Entry(a, font=("Helvetica", 12), show="*", width=30)
password_entry.pack()


#login 
def sign ():
    username = username_entry.get()
    password = password_entry.get()

    if password == "c":
        open_new_window()
    else:
        welcome_message = "Incorrect username or password. Please try again."
        welcome_label.config(text=welcome_message)


login_button = ttk.Button(a, text="Login", command=sign)
login_button.pack(pady=20)

#welcome label
welcome_label = ttk.Label(a, text="", font=("Helvetica", 12), foreground="red", background="#222222")
welcome_label.pack(pady=10)


def open_new_window():
    new_window = tk.Toplevel()
    new_window.title("HOME PAGE")
    new_window.geometry("350x400")
    new_window.resizable(0, 0)
    new_window.configure(bg='#222222')
   

    button = tk.Button(new_window, text="SERIES", bd=5,font=("Calibri", 14),bg="black",fg="white", command=wrt_wdw)
    button.pack(pady=30)

    button2 = tk.Button(new_window, text="MOVIES",bd=5, font=("Calibri", 14), bg="black",fg="white", command=create_another_window)
    button2.pack(pady=30)

    button3 = tk.Button(new_window, text="CLOSE", bd= 5,font=("Calibri", 14),bg="black",fg="white", command=a.destroy)
    button3.pack(pady=30)

    
    welcome_label = ttk.Label(new_window, text=f"Welcome to CINIPHILIA!!", font=("Helvetica", 12), foreground="indian red", background="#222222")
    welcome_label.pack(pady=30)

def wrt_wdw():
    wrt_wdw = tk.Toplevel()
    wrt_wdw.title("SERIES")
    wrt_wdw.geometry("750x400")
    wrt_wdw.resizable(0,0)

 # Define the canvas and scrollbar widgets
    canvas = tk.Canvas(wrt_wdw, height=500, width=800, bg="#222222")
    
    scrollbar = ttk.Scrollbar(wrt_wdw, orient="vertical", command=canvas.yview)
    canvas.config(yscrollcommand=scrollbar.set)
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Create a frame inside the canvas to hold the images
    frame = tk.Frame(canvas, bg="#222222")
    
    frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Define the Series Posters
    poster_paths = [
        "C:\\Users\\ELCOT\\Desktop\\Project ThisIsCinema\\Templates\\BrBa.jfif",
        "C:\\Users\\ELCOT\\Desktop\\Project ThisIsCinema\\Templates\\GOT.jfif",
        "C:\\Users\\ELCOT\\Desktop\\Project ThisIsCinema\\Templates\\BCS.jfif"
        ]

    # Load and resize the posters, and add them to the frame
    for i, path in enumerate(poster_paths):
        image = Image.open(path)
        image = image.resize((200, 300))
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(frame, image=photo,bd=5,bg="black")
        label.grid(row=i//3, column=i%3, padx=20, pady=20)
        label.image = photo

    #movie opening buttons
    save_button1=tk.Button(wrt_wdw,text="BREAKING BAD",command=BrBa,bg="black",fg="white",bd=5)
    save_button1.place(x=80,y=350)

    save_button2=tk.Button(wrt_wdw,text="GAME OF THRONES",command=GOT,bg="black",fg="white",bd=5)
    save_button2.place(x=320,y=350)

    save_button3=tk.Button(wrt_wdw,text="BETTER CALL SAUL",command=BCS,bg="black",fg="white",bd=5)
    save_button3.place(x=590,y=350)

#links of the Series
    
def BrBa ():
     webbrowser.open("https://en.wikipedia.org/wiki/Breaking_Bad")

def GOT ():    
     webbrowser.open("https://en.wikipedia.org/wiki/Game_of_Thrones")

def BCS ():    
     webbrowser.open("https://en.wikipedia.org/wiki/Better_Call_Saul")


# Define label and photo variables outside the function
def create_another_window():
    another_window = tk.Toplevel()
    another_window.title("MOVIES")
    another_window.geometry("750x400")
    another_window.resizable(0,0)

    # Define the canvas and scrollbar widgets
    canvas = tk.Canvas(another_window, height=500, width=800, bg="#222222")
    scrollbar = ttk.Scrollbar(another_window, orient="vertical", command=canvas.yview)
    canvas.config(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Create a frame inside the canvas to hold the images
    frame = tk.Frame(canvas, bg="#222222")
    frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Define the Movie Posters
    poster_paths = ["C:\\Users\\ELCOT\\Desktop\\Project ThisIsCinema\\Templates\\Nayakan1987.jfif",
                    "C:\\Users\\ELCOT\\Desktop\\Project ThisIsCinema\\Templates\\TSR1994.jfif",
                    "C:\\Users\\ELCOT\\Desktop\\Project ThisIsCinema\\Templates\\Inception.jfif"
                    ]

    # Load and resize the posters, and add them to the frame
    for i, path in enumerate(poster_paths):
        image = Image.open(path)
        image = image.resize((200, 300))
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(frame, image=photo,bd=5,bg="black")
        label.grid(row=i//3, column=i%3, padx=20, pady=20)
        label.image = photo

    #movie opening buttons
    save_button1=tk.Button(another_window,text="NAYAKAN",command=Nayakan,bd=5,bg="black",fg="white")
    save_button1.place(x=80,y=350)

    save_button2=tk.Button(another_window,text="THE SHAWSHANK REDEMPTION",command=TSR,bd=5,bg="black",fg="white")
    save_button2.place(x=280,y=350)

    save_button3=tk.Button(another_window,text="INCEPTION",command=Inception,bg="black",bd=5,fg="white")
    save_button3.place(x=575,y=350)

#links of the movies
    
def Nayakan ():
     webbrowser.open("https://en.wikipedia.org/wiki/Nayakan")

def TSR ():    
     webbrowser.open("https://en.wikipedia.org/wiki/The_Shawshank_Redemption")

def Inception ():    
     webbrowser.open("https://en.wikipedia.org/wiki/Inception")



a.mainloop()







