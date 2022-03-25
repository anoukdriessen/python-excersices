import time
import threading
import tkinter as tk
from tkinter import ttk
from datetime import date

DEBUG = False

FONT = "Roboto"
FONT_S = (FONT, 11)
FONT_M = (FONT, 16)
FONT_L = (FONT, 50)

NOT_STARTED = 0
BUSY = 1
FINISHED = 2

class App:
    def __init__(self):
        # empty list to store sessions
        self.sessions_list = []
        # set default values
        self.sessions_list.append([1, 1])
        self.sessions_list.append([2, 0])

        # create the screen
        self.root = tk.Tk()
        self.root.geometry("400x300")
        self.root.title("RemindMe")
        # TODO set clock.png as icon

        # app variables
        self.time = tk.StringVar()
        self.time.set("60")
        self.sessions = tk.StringVar()
        self.sessions.set("2")
        self.message = tk.StringVar()
        self.message.set(f"Op de planning: {self.sessions.get()} sessies in {self.time.get()} minuten")
        self.current_session = tk.IntVar()
        self.current_session.set(1)
        self.nr_sessions = tk.IntVar()
        self.nr_sessions.set(len(self.sessions_list))
        self.counter = tk.StringVar()
        self.counter.set("25:00")

        # app styling
        self.style = ttk.Style()
        self.style.configure("TNotebook.Tab", font=FONT_S)
        self.style.configure("TButton", font=FONT_S)

        # create the tabs
        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill = "both", pady=5, expand=True)

        # TAB 1: Main tab
        self.mainTab = ttk.Frame(self.tabs)
        self.mainTab_label = ttk.Label(self.mainTab, text="Welkom bij RemindMe", font=FONT_M)
        self.mainTab_label.pack(pady=5)
        self.grid_layout = ttk.Frame(self.mainTab)
        self.grid_layout.pack()

        self.total_time_label = ttk.Label(self.grid_layout, text="tijd (in minuten)", font=FONT_S)
        self.total_time_label.grid(row=0, column=0)
        self.total_time = ttk.Entry(self.grid_layout, width=10, font=FONT_S)
        self.total_time.grid(row=0, column=1)
        self.total_time_btn = ttk.Button(self.grid_layout, text=">", command=self.submit)
        self.total_time_btn.grid(row=0, column=2)

        self.result = ttk.Label(self.mainTab, textvariable=self.message, font=FONT_S)
        self.result.pack(pady=5)

        self.sessions_layout = ttk.Frame(self.mainTab, width="400")
        self.sessions_layout.pack()
        self.current_label = ttk.Label(self.sessions_layout, text="Sessie", font=FONT_M)
        self.current_label.grid(row=0, column=0)
        self.current_session_label = ttk.Label(self.sessions_layout, textvariable=self.current_session, font=FONT_M)
        self.current_session_label.grid(row=0, column=1)
        self.current_total_divider = ttk.Label(self.sessions_layout, text="/", font=FONT_M)
        self.current_total_divider.grid(row=0, column=2)
        self.total_session_label = ttk.Label(self.sessions_layout, textvariable=self.nr_sessions, font=FONT_M)
        self.total_session_label.grid(row=0, column=3)

        self.counter_label = ttk.Label(self.mainTab, textvariable=self.counter, font=FONT_L)
        self.counter_label.pack()

        self.start_session_btn = ttk.Button(self.mainTab, text="Start", command=self.start_timer_thread, padding=5)
        self.start_session_btn.pack()

        # TODO lees data uit bestand om de data van de afgelopen dagen weer te geven
        self.stats = ttk.Frame(self.tabs, width=600, height=100)
        self.stats_label = ttk.Label(self.stats, text="Stats van de afgelopen 7 dagen", font=FONT_S)
        self.stats_label.pack(pady=10)

        self.tabs.add(self.mainTab, text="Home")
        self.tabs.add(self.stats, text="Stats")

        self.total_sessions_today = 0
        self.total_finished_sessions_today = 0

        self.started = False
        self.pauzed = False
        self.stopped = False

        self.root.mainloop()


    def submit(self):
        self.time.set(self.total_time.get())
        self.sessions.set(round(int(self.time.get()) / 30))

        nr_of_sessions = int(self.sessions.get())

        sessionMsg = "sessie"
        if nr_of_sessions > 1:
            sessionMsg += "s"

        if DEBUG: print(f"{self.time.get()} minuten geeft {self.sessions.get()} {sessionMsg}")
        self.message.set(f"Op de planning: {self.sessions.get()} {sessionMsg} in {self.time.get()} minuten")

        # make sure to start with empty list
        self.sessions_list.clear()
        self.current_session.set(1) # start again with session 1
        for num in range(nr_of_sessions):
            # add item to sessions list [nr, status]
            self.sessions_list.append([num + 1, NOT_STARTED])
        if DEBUG: print(self.sessions_list)
        self.nr_sessions.set(len(self.sessions_list))

    def start_timer_thread(self):
        thread = threading.Thread(target=self.start_timer)
        thread.start()

    def start_timer(self):
        # in case stopped was true make false
        self.stopped = False
        # start session / add one to nr of total sessions
        self.started = True
        self.total_sessions_today += 1
        self.sessions_list[self.current_session.get()-1][1] = 1
        self.start_session_btn.text="Stop"
        self.start_session_btn.command=self.stop
        # start countdown
        # total_seconds = 60 * 1
        total_seconds = 10
        self.start_countdown(total_seconds= total_seconds)
        if not self.stopped:
            self.total_finished_sessions_today += 1
            self.sessions_list[self.current_session.get()-1][1] = 2
            # go to next session
            finished = True
            if self.current_session.get() + 1 <= len(self.sessions_list):
                # finish current session
                self.current_session.set(self.current_session.get() + 1) 
                self.sessions_list[self.current_session.get()-1][1] = 1
                finished = False

            if DEBUG: print(f"countdown finished, finished {self.total_finished_sessions_today} sessions today, full status {self.sessions_list}, next session nr {self.current_session.get()}")
            if self.current_session.get() <= self.nr_sessions.get() and not finished:
                # TODO alert user break has started
                if self.current_session.get() % 4 == 0: 
                    if DEBUG: print("starting long break")
                    # user gets long break
                    total_seconds = 10
                    self.start_countdown(total_seconds=total_seconds)
                else:
                    if DEBUG: print("starting short break")
                    # user gets short break
                    total_seconds = 5
                    self.start_countdown(total_seconds=total_seconds)   

                self.start_timer()    
            else:
                # user is finished
                if DEBUG: print("finished all sessions")
                self.counter.set("DONE")
                self.current_session.set(1)
                self.appendData(date = str(date.today()), started_sessions=self.total_sessions_today, finished_sessions=self.total_finished_sessions_today)

    def start_countdown(self, total_seconds):
        if DEBUG: print(f"Starting countdown for {total_seconds} seconds")
        while total_seconds > 0 and not self.stopped:
            minutes, seconds = divmod(total_seconds, 60)
            self.counter.set(f"{minutes:02d}:{seconds:02d}")
            self.root.update()
            time.sleep(1)
            total_seconds -= 1
            
    def appendData(self, date, started_sessions, finished_sessions):
        with open("remind_me_to_switch/my_data.txt", mode="a") as f:
            f.write(f"\n[{date}] completed {finished_sessions} of {started_sessions} sessions")        

    def stop(self):
        pass

    def reset_clock(self):
        pass

    def pass_clock(self):
        pass


App()        