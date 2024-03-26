from fastapi import HTTPException

class RequestResponse:
    def response(self, data, status_code: int):
        raise HTTPException(
            status_code, 
            detail=data,
        )
    def error(self, message: str, status_code: int):
        raise HTTPException(
            status_code, 
            detail=f"Error: {message}"
        )