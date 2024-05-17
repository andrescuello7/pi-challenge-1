from typing import List
from fastapi import APIRouter
from fastapi.params import Depends, Depends
from models.character_model import CharacterModel
from models.eye_color_model import EyeColorModel
from schemas.character_schema import CharacterSchema
from db_config import Session, get_db

router = APIRouter()

@router.get('/api/character/getAll', response_model=List[CharacterSchema])
def find_all_characters(db: Session = Depends(get_db)): # type: ignore
    characters = db.query(CharacterModel).all()
    if characters:
        characters_with_eye_color = []
        for character in characters:
            eye_color = db.query(EyeColorModel).filter_by(id=character.eye_color_id).first()
            if eye_color:
                character_with_eye_color = {
                    "id": character.id,
                    "name": character.name,
                    "height": character.height,
                    "mass": character.mass,
                    "hair_color": character.hair_color,
                    "skin_color": character.skin_color,
                    "created_at": character.created_at,
                    "eye_color_id": character.eye_color_id,
                    "eye_color": {
                        "id": eye_color.id,
                        "color": eye_color.color
                    }
                }
                characters_with_eye_color.append(character_with_eye_color)
        return characters_with_eye_color
    return {'error': f'in show character'}

@router.get('/api/character/color/getAll')
def find_all_colors(db: Session = Depends(get_db)): # type: ignore
    colors = db.query(EyeColorModel).all()
    if colors:
        return colors
    return {'error': f'in show characters'}

@router.get('/api/character/get/{name}', response_model=CharacterSchema)
def find_character_by_name(name: str, db: Session = Depends(get_db)): # type: ignore
    character = db.query(CharacterModel).filter_by(name=name).first()
    if character:
        eye_color = db.query(EyeColorModel).filter_by(id=character.eye_color_id).first()
        if eye_color:
            return {
                "id": character.id,
                "name": character.name,
                "height": character.height,
                "mass": character.mass,
                "hair_color": character.hair_color,
                "skin_color": character.skin_color,
                "created_at": character.created_at,
                "eye_color_id": character.eye_color_id,
                "eye_color": {
                    "id": eye_color.id,
                    "color": eye_color.color
                }
            }
    return {'error': f'get characters for name'}

@router.get('/api/character/get/identify/{id}', response_model=CharacterSchema)
def find_character_by_id(id: int, db: Session = Depends(get_db)): # type: ignore
    character = db.query(CharacterModel).filter_by(id=id).first()
    if character:
        eye_color = db.query(EyeColorModel).filter_by(id=character.eye_color_id).first()
        if eye_color:
            return {
                "id": character.id,
                "name": character.name,
                "height": character.height,
                "mass": character.mass,
                "hair_color": character.hair_color,
                "skin_color": character.skin_color,
                "created_at": character.created_at,
                "eye_color_id": character.eye_color_id,
                "eye_color": {
                    "id": eye_color.id,
                    "color": eye_color.color
                }
            }
    return {'error': f'get characters for ID'}

@router.post('/api/character/add')
def create_character(req: CharacterSchema, db: Session = Depends(get_db)): # type: ignore
    if req.eye_color:
        response = CharacterModel(
            name=req.name,
            mass=req.mass,
            height=req.height,
            skin_color=req.skin_color,
            hair_color=req.hair_color,
            eye_color_id=req.eye_color_id,
            eye_color=EyeColorModel(
                color=req.eye_color.color
            )
        )
        db.add(response)
        db.commit()
        db.refresh(response)
        return response
    return {'error': f'get characters for ID'}

@router.delete('/api/character/delete/{id}')
def delete_character(id: int, db: Session = Depends(get_db)): # type: ignore
    character = db.query(CharacterModel).filter_by(id=id).first()
    if not character:
        return {"error": "in remove Character!"}
    eye_color = db.query(EyeColorModel).filter_by(id=character.eye_color_id).first()
    if eye_color:
        db.delete(character)
        db.delete(eye_color)
    db.commit()
    return {"message": "Character deleted successfully"}
