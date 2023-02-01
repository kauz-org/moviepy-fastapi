# instal depences
```commandline
poetry install
```

# run service
```commandline
poetry run uvicorn moviepy_api.main:app --reload
```

# Swagger
```
http://127.0.0.1:8000/api/docs#/movie/upload_api_auth_v1__post
```
