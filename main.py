import tkinter
import customtkinter
from pytube import YouTube
import threading


# Download Functions
def videoDownload():
    def download():
        try:
            userFeedback.configure(text='Downloading', text_color='green')
            ytLink = url.get()
            ytObject = YouTube(ytLink, on_progress_callback=on_progress)
            video = ytObject.streams.get_highest_resolution()
            video.download()
            title.configure(text=ytObject.title, text_color='white')
            finishLabel.configure(text='Downloaded', text_color='green')
            progressBar.set(0.0)  # Reset progress bar to 0
            pPercentage.configure(text='0%')  # Reset progress label to 0%

        except:
            finishLabel.configure(text='ERROR INVALID LINK', text_color='red')
            app.after(2000, lambda: finishLabel.configure(text=''))

        userFeedback.configure(text='')

    threading.Thread(target=download).start()


def audioDownload():
    def download():
        try:
            userFeedback.configure(text='Downloading', text_color='green')
            ytLink = url.get()
            ytObject = YouTube(ytLink, on_progress_callback=on_progress)
            audio = ytObject.streams.get_audio_only()
            audio.download()
            title.configure(text=ytObject.title, text_color='white')
            finishLabel.configure(text='Downloaded', text_color='green')
            progressBar.set(0.0)  # Reset progress bar to 0
            pPercentage.configure(text='0%')  # Reset progress label to 0%

        except:
            finishLabel.configure(text='ERROR INVALID LINK', text_color='red')
            app.after(2000, lambda: finishLabel.configure(text=''))

        userFeedback.configure(text='')

    threading.Thread(target=download).start()


# Progress Function
def on_progress(stream, chunk, bytes_remaining):
    totalSize = stream.filesize
    bytes_downloaded = totalSize - bytes_remaining
    percentage = (bytes_downloaded / totalSize) * 100
    per = str(int(percentage))
    pPercentage.configure(text=per + '%', text_color='yellow')
    pPercentage.update()

    progressBar.set(float(percentage) / 100)

    # Reset progress percentage to 0 when the download is completed
    if percentage == 100:
        pPercentage.configure(text='0%')


# Default System Settings
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

# App Frame
app = customtkinter.CTk()
app.geometry('720x480')
app.title('Youtube Converter')
app.resizable(False, False)

# UI Elements
title = customtkinter.CTkLabel(app, text='Insert URL', padx=5, pady=20)
title.pack()

# Link Input
url_data = tkinter.StringVar()
url = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_data)
url.pack()

# Finish Downloading
finishLabel = customtkinter.CTkLabel(app, text='')
finishLabel.pack()

# Progress Bar
userFeedback = customtkinter.CTkLabel(app, text='')
userFeedback.pack()

pPercentage = customtkinter.CTkLabel(app, text='0%')
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0.0)
progressBar.pack(padx=10, pady=10)

# Download Buttons
downloadVideo = customtkinter.CTkButton(app, text='Download MP4', command=videoDownload).pack(padx=20, pady=40)
downloadAudio = customtkinter.CTkButton(app, text='Download MP3', command=audioDownload).pack(padx=20, pady=10)

# Run App
app.mainloop()
