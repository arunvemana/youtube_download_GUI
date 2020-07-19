import youtube_dl
from tkinter import filedialog
import tkinter

download_location = ""


def best_audio():
    return {
        'format': 'bestaudio/best',
        'ignoreerrors': True,
        'outtmpl': download_location + '/%(title)s.%(mp3)s',
        'ffmpeglocation': './',
        'addmetadata': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        },
            {
            'key': 'FFmpegMetadata',
        }],
    }


def best_video():
    return {
        'format': 'bestvideo+bestaudio/best',
        'ignoreerrors': True,
        'outtmpl': download_location + '/%(title)s',
        'ffmpeglocation': './',
    }


def video_specific_quality(vid_quality):
    try:
        return {
            'format': 'bestvideo[height<={}]+bestaudio/best'.format(int(vid_quality)),
            'ignoreerrors': True,
            'outtmpl': download_location + '/%(title)s',
            'ffmpeglocation': './',
        }
    except ValueError:
        return {
            'format': 'bestvideo[height<=720]+bestaudio/best',
            'ignoreerrors': True,
            'outtmpl': download_location + '/%(title)s',
            'ffmpeglocation': './',
        }


def open_directory():
    global download_location
    download_location = filedialog.askdirectory()

    print(download_location)


def vid_download(ydl_opts, url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


root = tkinter.Tk()

root.title('Youtube Video Downloader')

tkinter.Button(root, text="Specify Directory",
               command=lambda: open_directory()).pack()

tkinter.Label(root, text="Enter Url").pack()
entry1 = tkinter.Entry(root, width=50)
entry1.pack()

tkinter.Button(root, text="Highest Quality Video",
               command=lambda: vid_download(best_video(), entry1.get())).pack()

tkinter.Button(root, text="Highest Quality Audio",
               command=lambda: vid_download(best_audio(), entry1.get())).pack()

tkinter.Label(
    root, text="Enter Video Quality (144, 240, 360, 480, 720, 1080 etc)").pack()
entry2 = tkinter.Entry(root, width=50)
entry2.pack()

tkinter.Button(root, text="Video With Specified Quality (default=720p)", command=lambda: vid_download(
    video_specific_quality(entry2.get()), entry1.get())).pack()

root.mainloop()