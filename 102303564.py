import sys
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
            audio = AudioSegment.from_mp3(f"clips/{file}")
            final_audio += audio

    final_audio.export(output_file, format="mp3")

def main():
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
        sys.exit(1)

    singer = sys.argv[1]

    try:
        num_videos = int(sys.argv[2])
        duration = int(sys.argv[3])
    except ValueError:
        print("NumberOfVideos and AudioDuration must be integers")
        sys.exit(1)

    output_file = sys.argv[4]

    if num_videos <= 10:
        print("NumberOfVideos must be greater than 10")
        sys.exit(1)

    if duration <= 20:
        print("AudioDuration must be greater than 20 seconds")
        sys.exit(1)

    print("Downloading videos...")
    download_audios(singer, num_videos)

    print("Cutting audio clips...")
    cut_audios(duration)

    print("Merging audio files...")
    merge_audios(output_file)

    print("Mashup created successfully 🎵")

if __name__ == "__main__":
    main()
