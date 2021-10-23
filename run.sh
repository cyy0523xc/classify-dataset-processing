docker rm -f classify-dataset-processing

docker run -d --name classify-dataset-processing \
    --restart always \
    -v "$PWD/app":/app \
    -p 20960:8000 \
    -w /app \
    uvicorn main:app --host 0.0.0.0 --reload