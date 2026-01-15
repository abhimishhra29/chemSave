from typing import Optional
from fastapi import APIRouter, File, UploadFile, HTTPException, Request

router = APIRouter()

@router.post("/identify-chemical")
async def identify_chemical(  
    request: Request,  
    front_image: Optional[UploadFile] = File(None),
    back_image: Optional[UploadFile] = File(None)
    ):
    """finds chemicals safety datasheet"""
    if not front_image and not back_image:
        raise HTTPException(400, "Upload front_image or back_image")
    
    img = front_image or back_image
    image_bytes = await img.read()
    graph_app = request.app.state.graph_app

    result = await graph_app.ainvoke(
        {
            "image_bytes": image_bytes,
            "ocr_text": None
        }
    )


    return {
            "ocr_text": result.get("ocr_text"),
            "product_name": result.get("product_name"),
            "product_code": result.get("product_code"),
            "cas_number": result.get("cas_number"),
            "manufacturer_name": result.get("manufacturer_name"),
            "manufacturer_url": result.get("manufacturer_url"),
            "sds_search_results": result.get("sds_search_results"),
            "validation_status": result.get("validation_status"),
    }