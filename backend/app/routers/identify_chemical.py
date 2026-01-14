from typing import Optional
from fastapi import APIRouter, File, UploadFile, HTTPException

router = APIRouter()

@router.post("/identify-chemical")
async def identify_chemical(  
    front_image: Optional[UploadFile] = File(None),
    back_image: Optional[UploadFile] = File(None)
    ):
    """finds chemicals safety datasheet"""
    if not front_image and not back_image:
        raise HTTPException(400, "Upload front_image or back_image")

    return {
        "front": front_image.filename if front_image else None,
        "back": back_image.filename if back_image else None, 
    }