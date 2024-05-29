# FastApi - Challenge

Challenge of API with framework FastAPI -> Python!
- URL [```ApiRest - Fastapi```](https://pi-challenge-fr.vercel.app)

![Preview Image](https://github.com/andrescuello7/pi-challenge-1/assets/72234490/38cc0f14-2d9a-439c-93bd-62fc9ef99aac)

##
#### Development:

```bash
git clone https://github.com/andrescuello7/pi-challenge-1
cd pi-challenge-1/

virtualenv -p python3.10.13 venv
source venv/bin/activate

python -m pip install -r requirements.txt

gunicorn app:app -w 4 -k uvicorn.workers.UvicornWorker
```

#### Swagger:
Added Swagger for default in FastAPI 
- Redirect for swagger in root route

![Preview Image](https://github.com/andrescuello7/pi-challenge-1/assets/72234490/3e29abdc-6c96-4498-9560-8ca5bedfd905)

##

#### Postman:
Add Postman for Docs and Request
- URL [```https://app.getpostman.com/```](https://app.getpostman.com/join-team?invite_code=20158f9e67cb3b741ec50311e33a0ce0&target_code=c5801ae90c43b4b0ab1e43e2c8c44383)


![Preview Image](https://github.com/andrescuello7/pi-fastapi-apirest/assets/72234490/3867aef6-5dc0-4af0-9112-c977d42dab4a)

##
