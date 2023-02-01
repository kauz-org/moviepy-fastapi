import os
from uuid import uuid4

from fastapi import APIRouter, File, UploadFile
from moviepy.editor import *

router = APIRouter(prefix="/api/auth/v1", tags=["movie"])


@router.post('/')
def upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        folder = f'storage{os.sep}{str(uuid4())}{os.sep}'
        os.mkdir(folder)
        filename = f'{folder}original'
        with open(f'{filename}.mp4', 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
    clip = VideoFileClip(f'{filename}.mp4')
    for x in [140, 320, 720, 1080]:
        final = clip.fx(vfx.resize, height=x)
        final.write_videofile(f'{folder}{x}.mp4', preset='slow')

    return {"message": f"Successfully uploaded {file.filename}"}
