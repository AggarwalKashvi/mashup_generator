# Mashup Generator 🎧
 
The application generates an audio mashup by downloading multiple YouTube videos of a given singer, extracting audio from them, trimming each clip to a fixed duration, and merging all clips into a single output file.

The project consists of:
- A **command-line based mashup generator (Program 1)**
- A **web-based mashup service using FastAPI (Program 2)**

---

## Project Objectives

- Automate the process of creating an audio mashup from YouTube videos
- Demonstrate the use of Python libraries for media processing
- Build a simple web service using FastAPI
- Design a user-friendly frontend interface
- Follow secure coding practices (no hardcoded credentials)

---

## Features

- Accepts the following user inputs:
  - Singer name
  - Number of videos (must be greater than 10)
  - Duration of each audio clip (must be greater than 20 seconds)
  - Email address (collected as per assignment requirement)
- Downloads audio from YouTube using search queries
- Converts videos to audio automatically
- Trims audio clips to the specified duration
- Merges all clips into a single mashup
- Generates output in ZIP format
- Clean and modern web-based UI
- Modular and reusable backend logic

---

## Tech Stack

### Backend
- Python 3
- FastAPI
- yt-dlp
- FFmpeg
- pydub

### Frontend
- HTML
- CSS
- Jinja2 Templates

### Tools
- Git & GitHub
- Virtual Environment (`venv`)

---

## Interface

<img width="497" height="527" alt="image" src="https://github.com/user-attachments/assets/d661491c-a134-4ca8-98bb-6263a1e3de85" />


