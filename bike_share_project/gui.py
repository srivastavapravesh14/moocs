import tkinter as tk
from tkinter import messagebox

from tkinter import font as tkFont 
from Chicago_GUI import Chicago
from NY_GUI import NY
from WASHINGTON_GUI import Washington

root = tk.Tk()
root.title("Bike Share")
root.geometry("1080x550")
root.configure(background = "#DDE7EB") 

C= Chicago()
N =NY()
W = Washington()

def open_function1(args):
    if args ==1:
        C.popular_time()
        
    if args ==2:
        C.popular_station()
        
    if args ==3:
        C.trip_duration()
        
    if args ==4:
        C.user_info()
        
def open_function2(args):
    if args ==1:
        N.popular_time()
        
    if args ==2:
        N.popular_station()
        
    if args ==3:
        N.trip_duration()
        
    if args ==4:
        N.user_info()

def open_function3(args):
    if args ==1:
        W.popular_time()
        
    if args ==2:
        W.popular_station()
        
    if args ==3:
        W.trip_duration()
        
    if args ==4:
        W.user_info()



#==============================================================================        
font1 = tkFont.Font(family = "Georgia", size = 30,\
                    weight ="bold")

font2 = tkFont.Font(family = "Georgia", size = 20)
font3 = tkFont.Font(family = "Georgia", size = 12)

#============================================================================== 

#============================================================================== 
Label1 = tk.Label(master = root, text = "Bike Share Information "\
                       ,background = "#DDE7E7", font = font1\
                           ,foreground = "#000000  ")
Label1.place(relx = 0.25, rely = 0.02)
#============================================================================== 


#==============================================================================   
#_______Label_buttons_cities________
#Labels
chicago = tk.Label(master = root, text = "Chicago :"\
                        ,background = "#DDE7E7", font = font2\
                           ,foreground = "#000000  ")
chicago.place(relx = 0.03, rely = 0.28)

newyork = tk.Label(master = root, text = "New York :"\
                        ,background = "#DDE7E7", font = font2\
                           ,foreground = "#000000  ")
newyork.place(relx = 0.03, rely = 0.41)

washington = tk.Label(master = root, text = "Washington :"\
                        ,background = "#DDE7E7", font = font2\
                           ,foreground = "#000000  ")
washington.place(relx = 0.03, rely = 0.53)

#buttons
#1.time        
chicago_time = tk.Button(master = root, text = "Popular Time"\
               ,background = "#32BBF4", font = font3,foreground = "#000000"\
               ,borderwidth = 1,command = lambda:open_function1(1))
chicago_time.place(relx = 0.25, rely = 0.29)   

ny_time = tk.Button(master = root, text = "Popular Time"\
                                ,background = "#32BBF4", font = font3\
        ,foreground = "#000000", borderwidth = 1 ,command = lambda:open_function2(1))
ny_time.place(relx = 0.25, rely = 0.42)

wash_time = tk.Button(master = root, text = "Popular Time"\
                                ,background = "#32BBF4", font = font3\
    ,foreground = "#000000", borderwidth = 1,command = lambda:open_function3(1))
wash_time.place(relx = 0.25, rely = 0.55)

#2.Start and End Points        
chicago_station = tk.Button(master = root, text = "Popular Stations"\
                            ,background = "#32BBF4", font = font3\
                            ,foreground = "#000000", borderwidth = 1,command = lambda:open_function1(2))
chicago_station.place(relx = 0.42, rely = 0.29)   

ny_station = tk.Button(master = root, text = "Popular Stations"\
                                ,background = "#32BBF4", font = font3\
            ,foreground = "#000000", borderwidth = 1 ,command = lambda:open_function2(2))
ny_station.place(relx = 0.42, rely = 0.42)

wash_station = tk.Button(master = root, text = "Popular Stations"\
                                ,background = "#32BBF4", font = font3\
 ,foreground = "#000000", borderwidth = 1,command = lambda:open_function3(2))
wash_station.place(relx = 0.42, rely = 0.55)

#3.Trip Duration        
chicago_station = tk.Button(master = root, text = "Trip Duration"\
                                ,background = "#32BBF4", font = font3\
                ,foreground = "#000000", borderwidth = 1,command = lambda:open_function1(3))
chicago_station.place(relx = 0.61, rely = 0.29)   

ny_station = tk.Button(master = root, text = "Trip Duration"\
                                ,background = "#32BBF4", font = font3\
            ,foreground = "#000000", borderwidth = 1 ,command = lambda:open_function2(3))
ny_station.place(relx = 0.61, rely = 0.42)

wash_station = tk.Button(master = root, text = "Trip Duration"\
                                ,background = "#32BBF4", font = font3\
        ,foreground = "#000000", borderwidth = 1,command = lambda:open_function3(3))
wash_station.place(relx = 0.61, rely = 0.55)

#4. User Information        
chicago_station = tk.Button(master = root, text = "User Information"\
                                ,background = "#32BBF4", font = font3\
            ,foreground = "#000000", borderwidth = 1,command = lambda:open_function1(4))
chicago_station.place(relx = 0.78, rely = 0.29)   

ny_station = tk.Button(master = root, text = "User Information"\
                                ,background = "#32BBF4", font = font3\
        ,foreground = "#000000", borderwidth = 1,command = lambda:open_function2(4))
ny_station.place(relx = 0.78, rely = 0.42)

wash_station = tk.Button(master = root, text = "User Information"\
                                ,background = "#32BBF4", font = font3\
            ,foreground = "#000000", borderwidth = 1,command = lambda:open_function3(4))
wash_station.place(relx = 0.78, rely = 0.55)

#5. Exit
def exit_window():
    root.destroy()
    
Exit = tk.Button(master = root, text = "Exit"\
                                ,background = "#F49332", font = font3\
                                    ,foreground = "#000000", borderwidth = 1\
                                        ,width = 8, command = exit_window)
Exit.place(relx = 0.25, rely = 0.70)

#6. Information
def Information():
    
    quote = """This software tells the information about bike sharing data.
It has been build upon the nanodegree project from Udacity for "Programming for Data Science Nanodegree Course."\n 
The developer of this software was not enrolled in the course instead he utilized the open source code from github repository for this project.
    """
    messagebox.showinfo("Information", quote)
    
        
    

Info = tk.Button(master = root, text = "Information"\
                                ,background = "#F49332", font = font3\
                                    ,foreground = "#000000", borderwidth = 1\
                                        ,width = 10, command = lambda:Information())
Info.place(relx = 0.25, rely = 0.15)       
#============================================================================== 
        
        
        
        
        

root.mainloop()        
        
