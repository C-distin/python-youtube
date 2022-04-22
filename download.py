from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy import *
from moviepy.editor import VideoFileClip


# Functions
def select_folder():
    """
    Select folder to save files
    """
    folder = filedialog.askdirectory()
    folder_label.config(text=folder)


def download_best_video():
    """
    Download YouTube Videos of the highest quality
    """
    # Get YouTube URL
    get_path = link_path.get()
    # Get User Selected Folder
    user_path = folder_label.cget("text")

    # Download Best Quality Video
    best = YouTube(
        get_path).streams.get_highest_resolution().download(user_path)
    best_quality = VideoFileClip(best)
    best_quality.close()


def download_low_video():
    """
    Download YouTube Videos of the lowest quality
    """
    # Get YouTube URL
    get_path = link_path.get()
    # Get User Selected Folder
    user_path = folder_label.cget("text")

    # Download Low Quality Video
    low = YouTube(
        get_path).streams.get_lowest_resolution().download(user_path)
    low_quality = VideoFileClip(low)
    low_quality.close()


screen = Tk()
title = screen.title("YouTube Downloader")

canvas = Canvas(screen, width=400, height=400)
canvas.pack()

# Add YouTube logo
logo = PhotoImage(file="youtube1.png")
# Resize Logo
logo = logo.subsample(2, 2)
canvas.create_image(200, 60, image=logo)

# Link Field
link_path = Entry(screen, width=50)
link_label = Label(screen, text="Enter YouTube Link: ", font=("Hack NF", 12))

# Add Link Widgets
canvas.create_window(200, 140, window=link_label)
canvas.create_window(200, 170, window=link_path)

# Select Folder
folder_label = Label(
    screen, text="Select Download Folder: ", font=("Hack NF", 9))
folder_btn = Button(screen, text="Select Folder", command=select_folder)

# Add Folder Widgets
canvas.create_window(200, 220, window=folder_label)
canvas.create_window(200, 250, window=folder_btn)

# Add Download Button
download_best_button = Button(
    screen, text="Download Best Quality", command=download_best_video)
download_worst_button = Button(
    screen, text="Download Worst Quality", command=download_low_video)

# Add Download Button Widgets
canvas.create_window(100, 300, window=download_best_button)
canvas.create_window(300, 300, window=download_worst_button)

screen.mainloop()
