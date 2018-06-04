from pynput import keyboard
from tkinter import Tk
import tkinter as tk
from time import sleep
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


# The key combination to check
#keyboard.KeyCode.from_char('x')
COMBINATION = {keyboard.Key.ctrl,keyboard.Key.shift,keyboard.KeyCode.from_char('M')}

# The currently active modifiers
current = set()

def get_meaning(word):
    req = Request('https://www.google.com/search?q=define+'+str(word), headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()

    sub = 'Definition'
    soup = BeautifulSoup(page, 'html.parser')    
    spans = soup.find_all('span')
    # create a list of lines corresponding to element texts
    lines = [span.get_text() for span in spans if sub in span.get_text()]  
    print(lines)  
    dfn=lines[0]
    if dfn:       
        return dfn
    else:
        return "not found"

    # import requests
    # url = 'https://googledictionaryapi.eu-gb.mybluemix.net/?define=library'
    # resp = requests.get(url=url)
    # data = resp.json()
    # print(data["meaning"]["noun"][0]["definition"])
    # print(data["meaning"]["noun"][0]["example"])

def create_window(result):
    root = tk.Tk()
    

    means=get_meaning(result)
    tk.Label(root, 
             text=means,
             fg = "light green",
             bg = "dark green",
             font = "Helvetica 16 bold italic").pack()
    

    

    root.mainloop()

def on_press(key):
	#print(str(key)+' pressed')
    print(str(key)+' pressed')
    global COMBINATION
    global current
    if key in COMBINATION:
        current.add(key)

        if all(k in current for k in COMBINATION):
            print('All modifiers active!')
           
            r=Tk()
            r.withdraw()


            while not r.selection_get(selection="CLIPBOARD"):
                sleep(0.1)

            result=r.selection_get(selection="CLIPBOARD")
            
           
            #r.clipboard_clear()
            r.destroy()
            create_window(result)
            print(result)


    if key == keyboard.Key.esc:
        
        listener.stop()


def on_release(key):
    try:
        current.remove(key)
        
    except KeyError:
        pass


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    
    listener.join()





