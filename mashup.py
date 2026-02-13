import os
import yt_dlp
from pydub import AudioSegment

def download_audios(singer, num_videos):
    os.makedirs("downloads", exist_ok=True)
    search_query = f"ytsearch{num_videos}:{singer}"

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'quiet': True,
        'nocheckcertificate': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_query])

def cut_audios(duration):
    os.makedirs("clips", exist_ok=True)
    for file in os.listdir("downloads"):
        if file.endswith(".mp3"):
            audio = AudioSegment.from_mp3(f"downloads/{file}")
            clip = audio[:duration * 1000]
            clip.export(f"clips/{file}", format="mp3")

def merge_audios(output_file):
    final_audio = AudioSegment.empty()
    for file in os.listdir("clips"):
        if file.endswith(".mp3"):
            final_audio += AudioSegment.from_mp3(f"clips/{file}")
    final_audio.export(output_file, format="mp3")
