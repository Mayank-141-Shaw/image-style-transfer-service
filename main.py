from fastapi import FastAPI, UploadFile, Response, File
from fastapi.responses import FileResponse
from pathlib import Path
from model import generate_styled_image

app = FastAPI()

@app.get("/")
async def root():
    return { "msg" : "Send both content and style images to post request at this same path" }

@app.post(path="/")
async def output(
    content_image: UploadFile, 
    style_image: UploadFile
):
    style_image_contents = style_image.file.read()
    content_image_contents = content_image.file.read()
    generate_styled_image(content_image=content_image_contents, style_image=style_image_contents)

    res_path = Path('./save/generated_img.jpg')
    if not res_path.is_file():
        return {"error":"Image not found on server"}
    
    return FileResponse(res_path)