The api project can be built and run with the following commands
```
docker build -t api -f ./projects/api/Dockerfile .
docker run api
```

The api can be run locally with
```
uv run fastapi dev bases/foo/api/core.py
```
