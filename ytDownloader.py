from pytube import YouTube

VIDEO_URL = input("Digite a URL do video: ")

yt = YouTube(VIDEO_URL)
audio = yt.streams.filter(only_audio=True)[0]
audio.download()
