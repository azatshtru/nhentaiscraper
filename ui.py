import tkinter as tk
import tkinter.font as font

from tkinter import messagebox
from tkinter.ttk import Progressbar

import re
import scraper
import threading

_scraper = scraper.scraper()

btn = None

def keep_flat (event):
    if event.widget is btn:
        event.widget.config(relief='flat')

def interface ():
    global btn

    root = tk.Tk()
    root.title('N-hentai Scraper')
    root.geometry("300x400")
    root.configure(bg='#101010')
    root.resizable(False, False)
    root.iconbitmap('res/ahegao.ico')

    photo = tk.PhotoImage(file = "res/collage1.png")

    w = tk.Label(root, image=photo)
    w.pack()

    _font = font.Font(family='Verdana', weight='bold')
    _font2 = font.Font(family='Courier New', size=10)
    _font3 = font.Font(family='Courier New', size=11)
    _font4 = font.Font(family='Verdana', size=9, weight='bold')

    end_text = tk.Label(root, font=_font4, bg = '#121212', fg='white')
    end_text.place(relx=0.11, rely=0.3, relwidth = 0.799, relheight=0.15)

    instruction_text = tk.Label(root, text="Enter index of the manga:", font=_font2)
    instruction_text.place(relx=0.11, rely=0.28, relwidth = 0.799, relheight=0.07)

    doujin_index = tk.StringVar()
    text_field = tk.Entry(root, textvariable=doujin_index, font=('Courier New', 20, 'bold'), bg='#101010', fg='#efefef', bd="0px")
    text_field.place(relx=0.11, rely=0.35, relwidth = 0.8, relheight=0.1)

    progress = Progressbar(root, orient='horizontal', length=100, mode='determinate')
    progress.place(relx=0.078, rely=0.65, relwidth = 0.85, relheight=0.08)

    def update_bar ():
        while(True):
            _scraper.get_perc != None
            perc = _scraper.get_perc()
            progress['value'] = perc
            root.update_idletasks()
            if(perc > 99):
                root.quit()
                break
        
    def send_index (index):
        nh_index = index
        t2 = threading.Thread(target=update_bar, args=())
        t2.start()

        _scraper.scrape_comic(nh_index)

    def submit():
        entered_nums = text_field.get()
        if(re.match('^[0-9]*$', entered_nums) and entered_nums != None and entered_nums != ''):
            
            t1 = threading.Thread(target=send_index, args=(entered_nums,))
            t1.start()

            end_text['text'] = "Your requested manga\nwith index: {0}\nwill be downloaded\nto your desktop.".format(entered_nums)
            instruction_text.destroy()
            btn.destroy()
            text_field.destroy()
            #root.quit()

        else: messagebox.showwarning("Invalid index", "Incorrect Doujin index entered, please enter valid index with numbers only.")

    btn = tk.Button(root, 
                    bg='#FF0060', fg='#FFFFFF',
                    relief='flat', command=submit,
                    text='DOWNLOAD MANGA',
                    activebackground="white", activeforeground="#FF0060", font=_font)
    btn.place(relx=0.078, rely=0.62, relwidth = 0.85, relheight=0.12)

    credit_text = tk.Label(root, text="made by azatshtru", font=_font3, bg = '#121212', fg='white')
    credit_text.place(relx=0, rely=0.93, relwidth = 1, relheight=0.07)

    root.bind('<Button-1>', keep_flat)

    root.mainloop()