import tkinter as tk
from tkinter import font as tkFont 
from computed_statistics import Stats 
from tkinter import messagebox


class NY:
    def popular_time(self):
        
        top = tk.Tk()
        top.title("Bike Share")
        top.geometry("300x350")
        top.configure(background = "#DDE7EB") 
        
        
        #==============================================================================        
        font1 = tkFont.Font(family = "Georgia", size = 20,\
                            weight ="bold")
        
        
        font3 = tkFont.Font(family = "Georgia", size = 12)
        #============================================================================== 
        
        #============================================================================== 
        Label1 = tk.Label(master = top, text = "NY Popular Time\n Information "\
                               ,background = "#DDE7E7", font = font1\
                                   ,foreground = "#000000  ")
        Label1.place(relx = 0.08, rely = 0.02)
        #============================================================================== 
        def plots_call(args):
            if args == 1:
                hour = Stats("new_york")
                fig1 = hour.popular_time_hours()
                
            if args == 2:
                day = Stats("new_york")
                fig1 = day.popular_time_days()
                
            if args == 3:
                months = Stats("new_york")
                fig1 = months.popular_time_months()
                
        
        
        #buttons
        #1.time        
        hours = tk.Button(master = top, text = "Popular Hours"\
                                        ,background = "#32BBF4", font = font3\
        ,foreground = "#000000", borderwidth = 1, width =14, command = lambda: plots_call(1))
        hours.place(relx = 0.08, rely = 0.19)   
        
        days = tk.Button(master = top, text = "Popular Days"\
                                        ,background = "#32BBF4", font = font3\
            ,foreground = "#000000", borderwidth = 1,width = 14, command = lambda: plots_call(2))
        days.place(relx = 0.08, rely = 0.32)
        
        months = tk.Button(master = top, text = "Popular Months"\
                                        ,background = "#32BBF4", font = font3\
        ,foreground = "#000000", borderwidth = 1,width = 14, command = lambda: plots_call(3))
        months.place(relx = 0.08, rely = 0.45)
        #5. Exit
        def exit_window():
            top.destroy()
        Exit = tk.Button(master = top, text = "Exit"\
                                        ,background = "#F49332", font = font3\
                                            ,foreground = "#000000", borderwidth = 1\
                                                ,width = 8, command = exit_window)
        Exit.place(relx = 0.08, rely = 0.62)
          
    def popular_station(self):
        top = tk.Tk()
        top.title("Bike Share")
        top.geometry("400x400")
        top.configure(background = "#DDE7EB") 
        
        
        #==============================================================================        
        font1 = tkFont.Font(family = "Georgia", size = 20,\
                            weight ="bold")
        
        
        font3 = tkFont.Font(family = "Georgia", size = 12)
        #============================================================================== 
        
        #============================================================================== 
        Label1 = tk.Label(master = top, text = "NY Popular Trip Stations "\
                               ,background = "#DDE7E7", font = font1\
                                   ,foreground = "#000000  ")
        Label1.place(relx = 0.08, rely = 0.02)
        #============================================================================== 
        
        
        def message_display(args):
            data = Stats("new_york")
            if args == 1:
                
                SS,_, _ = data.popular_trips_stations_stats()
                quote1 = f"{SS} is the most popular Start Station"
                messagebox.showinfo("Information", quote1)
                
                
            if args == 2:
                _,ES, _ = data.popular_trips_stations_stats()
                quote1 = f"{ES} is the most popular End Station"
                messagebox.showinfo("Information", quote1)
                
            if args == 3:
                _,_, FS = data.popular_trips_stations_stats()
                quote1 = f"{FS} is the most Frequent route"
                messagebox.showinfo("Information", quote1)
        #buttons
        #1.Stations        
        start = tk.Button(master = top, text = "Popular Start Points"\
                                        ,background = "#32BBF4", font = font3\
                    ,foreground = "#000000", borderwidth = 1, width =22\
                , command = lambda: message_display(1))
        start.place(relx = 0.08, rely = 0.19)   
        
        end_points = tk.Button(master = top, text = "Popular End Points"\
                                        ,background = "#32BBF4", font = font3\
            ,foreground = "#000000", borderwidth = 1,width = 22\
                ,command = lambda: message_display(2))
        end_points.place(relx = 0.08, rely = 0.32)
        
        frequent_route = tk.Button(master = top, text = "Most frequent Route"\
                                        ,background = "#32BBF4", font = font3\
            ,foreground = "#000000", borderwidth = 1,width = 22\
                ,command = lambda: message_display(3))
        frequent_route.place(relx = 0.08, rely = 0.45)
        #2. Exit
        def exit_window():
            top.destroy()
        Exit = tk.Button(master = top, text = "Exit"\
                                        ,background = "#F49332", font = font3\
                                            ,foreground = "#000000", borderwidth = 1\
                                                ,width = 8, command = exit_window)
        Exit.place(relx = 0.08, rely = 0.62)
        
    def trip_duration(self):
        top = tk.Tk()
        top.title("Bike Share")
        top.geometry("300x300")
        top.configure(background = "#DDE7EB") 
        
        
        #==============================================================================        
        font1 = tkFont.Font(family = "Georgia", size = 20,\
                            weight ="bold")
        
        
        font3 = tkFont.Font(family = "Georgia", size = 12)
        #============================================================================== 
        
        #============================================================================== 
        Label1 = tk.Label(master = top, text = "NY Trip Durations "\
                               ,background = "#DDE7E7", font = font1\
                                   ,foreground = "#000000  ")
        Label1.place(relx = 0.08, rely = 0.02)
        #============================================================================== 
        #buttons
        
        def message_display2(args):
            data = Stats("new_york")
            if args == 1:
                
                MT,_ = data.trip_duration_stats()
                quote1 = f"{MT} is the total travel time"
                messagebox.showinfo("Information", quote1)
                
                
            if args == 2:
                _,AT = data.trip_duration_stats()
                quote1 = f"{AT} is the most popular End Station"
                messagebox.showinfo("Information", quote1)
                
            
        
        
        #1.Duration        
        total = tk.Button(master = top, text = "Total time"\
                                        ,background = "#32BBF4", font = font3\
        ,foreground = "#000000", borderwidth = 1, width =14\
            ,command = lambda:message_display2(1))
        total.place(relx = 0.08, rely = 0.19)   
        
        average = tk.Button(master = top, text = "Average Time"\
                                        ,background = "#32BBF4", font = font3\
            ,foreground = "#000000", borderwidth = 1,width = 14\
                ,command = lambda:message_display2(2))
        average.place(relx = 0.08, rely = 0.32)
        
        #2. Exit
        def exit_window():
            top.destroy()
        Exit = tk.Button(master = top, text = "Exit"\
                                        ,background = "#F49332", font = font3\
                                            ,foreground = "#000000", borderwidth = 1\
                                                ,width = 8, command = exit_window)
        Exit.place(relx = 0.08, rely = 0.62)  
        
    def user_info(self):
        top = tk.Tk()
        top.title("Bike Share")
        top.geometry("400x400")
        top.configure(background = "#DDE7EB") 
        
        
        #==============================================================================        
        font1 = tkFont.Font(family = "Georgia", size = 20,\
                            weight ="bold")
        
        
        font3 = tkFont.Font(family = "Georgia", size = 12)
        #============================================================================== 
        
        #============================================================================== 
        Label1 = tk.Label(master = top, text = "NY User Information "\
                               ,background = "#DDE7E7", font = font1\
                                   ,foreground = "#000000  ")
        Label1.place(relx = 0.08, rely = 0.02)
        #============================================================================== 
        #buttons
        def plots_call2(args):
            user = Stats("new_york")
            if args == 1:
                
                fig111 = user.user_info_stats()
                
            if args == 2:
                
                fig2222 = user.gender_stats()
                
            if args == 3:
                
                earliest_birth, latest_birth, common_birth = user.birth_stats()
                quote1 = f"{earliest_birth} is the earliest birth year in the dataset.\n{latest_birth} is the latest birth year in the dataset.\n {common_birth} is the most common birth year" 
                messagebox.showinfo("Information", quote1)
                
                
        
        
        #1.User Info        
        User_info = tk.Button(master = top, text = "Users"\
                                ,background = "#32BBF4", font = font3\
                                ,foreground = "#000000", borderwidth = 1, width =18\
                            , command = lambda: plots_call2(1))
        User_info.place(relx = 0.08, rely = 0.19)   
        
        gender = tk.Button(master = top, text = "Gender"\
                                        ,background = "#32BBF4", font = font3\
                            ,foreground = "#000000", borderwidth = 1,width = 18\
                                ,command = lambda: plots_call2(2))
        gender.place(relx = 0.08, rely = 0.32)
        
        birth_st = tk.Button(master = top, text = "Birth Stats"\
                                        ,background = "#32BBF4", font = font3\
                        ,foreground = "#000000", borderwidth = 1,width = 18\
                            ,command = lambda: plots_call2(3))
        birth_st.place(relx = 0.08, rely = 0.45)
        
        
        
        #2. Exit
        def exit_window():
            top.destroy()
        Exit = tk.Button(master = top, text = "Exit"\
                                        ,background = "#F49332", font = font3\
                                            ,foreground = "#000000", borderwidth = 1\
                                                ,width = 8, command = exit_window)
        Exit.place(relx = 0.08, rely = 0.62)
    
