from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import shutil
import zipfile
import os

from mashup import download_audios, cut_audios, merge_audios

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/mashup")
def create_mashup(
    singer: str = Form(...),
    videos: int = Form(...),
    duration: int = Form(...),
    email: str = Form(...)   # collected but NOT used
):
    try:
        if videos <= 10 or duration <= 20:
            return JSONResponse(
                status_code=400,
                content={"error": "Videos must be >10 and duration >20 seconds"}
            )

        output_file = "mashup.mp3"
        zip_file = "mashup.zip"

        # Clean old folders
        for folder in ["downloads", "clips"]:
            if os.path.exists(folder):
                shutil.rmtree(folder)

        os.makedirs("downloads", exist_ok=True)
        os.makedirs("clips", exist_ok=True)

        # Mashup pipeline
        download_audios(singer, videos)
        cut_audios(duration)
        merge_audios(output_file)

        # Zip output
        with zipfile.ZipFile(zip_file, "w") as zipf:
            zipf.write(output_file)

        return {
            "status": "Mashup created successfully",
            "note": "Email captured but delivery disabled",
            "zip_file": zip_file
        }

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )
