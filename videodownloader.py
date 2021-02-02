from tkinter import *
from pytube import YouTube

root = Tk()

root.geometry("400x350")

root.title("App for downloading YouTube videos.")

def download():
    try:
        myString.set("Downloading...")
        root.update()
        yt = YouTube(link.get())
        print(yt)
        stream = yt.streams.first()
        print(stream)
        stream.download()
        print(stream.download)
        link.set("Video Downloaded Successfully.")
    except Exception as e:
        print(e)
        myString.set("Error.")
        root.update()
        link.set("Enter correct link...")


#Creating the GUI.
Label(root, text="YouTube Video Downloader").pack()
myString = StringVar()
myString.set("Enter Link Below")
Entry(root, textvariable = myString, width = 40).pack(pady=10)
link = StringVar()
Entry(root, textvariable =link, width = 40).pack(pady=10)
#Button calls def download.
Button(root, text="Download Video", command=download).pack()
root.mainloop()
