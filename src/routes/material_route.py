import json
import os
import uuid

from bson import ObjectId
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from gridfs import GridFS

from src.db.db import get_material_collection, get_db
import aiofiles

router = APIRouter()

db = get_db()

materials_collection = get_material_collection()

fs = GridFS(db, collection="materials")


@router.post("/material/add")
async def add_material_record(title: str = Form(...), rating: float = Form(...),
                              delivery_time: str = Form(...),
                              cost_price: float = Form(...),
                              discount: float = Form(...),
                              in_file: UploadFile = File(...),
                              additional_fee: float = Form(...),
                              ):
    random_name = uuid.uuid4()
    async with aiofiles.open(f"uploads/materials_photo/{random_name}.jpg", "wb") as out_file:
        while True:
            content = await in_file.read(1024)
            if not content:
                break
            await out_file.write(content)

    photo_url = f"uploads/materials_photo/{random_name}.jpg"
    materials_collection.insert_one({"title": title, "rating": rating, "delivery_time": delivery_time,
                                     "cost_price": cost_price,
                                     "discount": discount,
                                     "thumbnail_url": photo_url,
                                     "additional_fee": additional_fee
                                     })

    return {"code": 200, "message": "Successfully added"}


@router.delete("/material/remove/{material_id}")
async def delete_material_record(material_id: str):
    material = materials_collection.find_one({"_id": ObjectId(material_id)})
    if material:
        thumbnail_url = material.get("thumbnail_url")
        if thumbnail_url:
            file_path = f"uploads/materials_photo/{thumbnail_url.split('/')[-1]}"
            if os.path.exists(file_path):
                os.remove(thumbnail_url)
        materials_collection.delete_one({"_id": ObjectId(material_id)})
        return {"code": 200, "message": "Successfully deleted"}
    else:
        return {"code": 200, "message": "No such record exists"}


@router.put("/material/update/{material_id}")
async def update_material(material_id: str, title: str = Form(None),
                          rating: int = Form(None),
                          delivery_time: str = Form(None),
                          cost_price: float = Form(None),
                          discount: float = Form(None),
                          additional_fee: float = Form(None),
                          in_file: UploadFile = File(None),
                          ):
    material = materials_collection.find_one({"_id": ObjectId(material_id)})
    if not material:
        raise HTTPException(status_code=404, detail="Material not found")

    if title:
        materials_collection.update_one({"_id": ObjectId(material_id)}, {"$set": {"title": title}})
        material["title"] = title

    if rating:
        materials_collection.update_one({"_id": ObjectId(material_id)}, {"$set": {"rating": rating}})
        material["rating"] = rating

    if delivery_time:
        materials_collection.update_one({"_id": ObjectId(material_id)}, {"$set": {"delivery_time": delivery_time}})
        material["delivery_time"] = delivery_time

    if cost_price:
        materials_collection.update_one({"_id": ObjectId(material_id)}, {"$set": {"cost_price": cost_price}})
        material["cost_price"] = cost_price

    if discount:
        materials_collection.update_one({"_id": ObjectId(material_id)}, {"$set": {"discount": discount}})
        material["discount"] = discount

    if additional_fee:
        materials_collection.update_one({"_id": ObjectId(material_id)}, {"$set": {"additional_fee": discount}})
        material["additional_fee"] = discount

    if in_file:
        random_name = uuid.uuid4()
        async with aiofiles.open(f"uploads/materials_photo/{random_name}.jpg", "wb") as out_file:
            while True:
                content = await in_file.read(1024)
                if not content:
                    break
                await out_file.write(content)

        thumbnail_url = f"uploads/materials_photo/{random_name}.jpg"
        materials_collection.update_one({"_id": ObjectId(material_id)}, {"$set": {"thumbnail_url": thumbnail_url}})
        material["thumbnail_url"] = thumbnail_url

    return {"code": 200, "message": "Successfully Updated"}


@router.get("/material/all")
async def list_materials():
    try:
        materials = list(materials_collection.find())
        for material in materials:
            material["_id"] = str(material["_id"])  # Convert ObjectId to string
        return {"data": materials}
    except Exception as e:
        return {"code": 500, "message": "Failed to retrieve artists", "error": str(e)}
