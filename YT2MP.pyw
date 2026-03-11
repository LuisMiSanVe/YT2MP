import tkinter as tk
from tkinter import ttk
import yt_dlp

# Button
def extract():
    global mp_var
    if mp_var.get() == "MP3":
        ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            }],
        }
    else:
        if mp_var.get() == "MP4":
            ydl_opts = {
                'format': 'best',
                'outtmpl': '%(title)s.%(ext)s',
            }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([entryURL.get()])

# GUI Setup
root = tk.Tk()
# Window
root.geometry("400x100")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.title("YT2MP - Youtube To MP3/4")
root.resizable(False, False)
# URL
tk.Label(root, text="Video URL:").grid(row=0, column=0, sticky='e', padx=5, pady=5)
entryURL = tk.Entry(root)
entryURL.grid(row=0, column=1, columnspan=2, sticky='we', padx=5, pady=5)
# Format selector
tk.Label(root, text="Format:").grid(row=1, column=0, sticky='e', padx=5, pady=5)
mp_var = tk.StringVar(value="MP3")
tk.Radiobutton(root, text="MP3 (Audio)", variable=mp_var, value="MP3").grid(row=1, column=1, sticky='we', padx=5, pady=5)
tk.Radiobutton(root, text="MP4 (Video)", variable=mp_var, value="MP4").grid(row=1, column=2, sticky='we', padx=5, pady=5)
# Extract
tk.Button(root,text="Extract",command=extract).grid(row=2, column=0, columnspan=3, sticky='we', padx=5, pady=5)

root.mainloop()