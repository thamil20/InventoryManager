from pathlib import Path
import shutil
import uuid
from fastapi import UploadFile, HTTPException
from PIL import Image, UnidentifiedImageError

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp", "gif", "bmp"}

def save_upload_file(upload_file: UploadFile, upload_dir: str) -> str:
    upload_path = Path(upload_dir)
    upload_path.mkdir(parents=True, exist_ok=True)

    original_name = Path(upload_file.filename or "")
    suffix = original_name.suffix.lower()
    if suffix not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Unsupported file extension")

    filename = f"{uuid.uuid4().hex}{suffix}"

    dest = upload_path / filename

    try:
        with open(dest, "wb") as buffer: #type: IO[bytes]
            upload_file.file.seek(0)
            shutil.copyfileobj(upload_file.file, buffer)
    except Exception as e:
        if dest.exists():
            dest.unlink()
        raise HTTPException(status_code=500, detail="Failed to save file") from e

    try:
        with Image.open(dest) as img:
            img.verify()
    except Exception:
        dest.unlink(missing_ok=True)
        raise HTTPException(status_code=500, detail="Uploaded file is not a valid image")

    return filename
