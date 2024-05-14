from typing import List
from fastapi import APIRouter
from fastapi.params import Depends, Depends

from src.config.database import Session, get_db
from enums.http_enum import HttpStatus

from src.models.character_model import CharacterModel
from src.models.eye_color_model import EyeColorModel
from src.schemas.character_schema import CharacterSchema

from enums.routes_enum import ROUTES_ENUM
from interfaces.i_request import RESPONSE_HTTP

router = APIRouter()

# Get for all characters of DB
@router.get(ROUTES_ENUM.GET_ALL_CHARACTERS, response_model=List[CharacterSchema])
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
    return RESPONSE_HTTP.error("Error in show characters", HttpStatus.BAD_REQUEST)

# Get for all eye_colors
@router.get(ROUTES_ENUM.GET_ALL_COLOR)
def find_all_colors(db: Session = Depends(get_db)): # type: ignore
    colors = db.query(EyeColorModel).all()
    if colors:
        return colors
    return RESPONSE_HTTP.error("Error in show characters", HttpStatus.BAD_REQUEST)

# Get Element for name of url parameter
@router.get(ROUTES_ENUM.GET_CHARACTER_BY_NAME, response_model=CharacterSchema)
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
    return RESPONSE_HTTP.error("Error get characters for name", HttpStatus.BAD_REQUEST)

# Get Element for ID of url parameter
@router.get(ROUTES_ENUM.GET_CHARACTER_BY_ID, response_model=CharacterSchema)
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
    return RESPONSE_HTTP.error("Error get characters for ID", HttpStatus.BAD_REQUEST)


# Create Character with model of schema
@router.post(ROUTES_ENUM.POST_CHARACTER)
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
    return RESPONSE_HTTP.error("Character not saved", HttpStatus.NOT_FOUND)


# Delete Character for ID of url parameter
@router.delete(ROUTES_ENUM.DELETE_CHARACTER)
def delete_character(id: int, db: Session = Depends(get_db)): # type: ignore
    character = db.query(CharacterModel).filter_by(id=id).first()
    if not character:
        return RESPONSE_HTTP.error("Error in remove Character!", HttpStatus.NOT_FOUND)
    eye_color = db.query(EyeColorModel).filter_by(id=character.eye_color_id).first()
    if eye_color:
        db.delete(character)
        db.delete(eye_color)

    db.commit()
    
    return {"message": "Character deleted successfully"}
