FROM python:3.12 as build
COPY --from=ghcr.io/astral-sh/uv:0.4.13 /uv /bin/uv
WORKDIR /src
COPY uv.lock pyproject.toml .
RUN uv export --no-emit-project --no-hashes > requirements.txt
COPY components/ ./components
COPY bases/ ./bases
COPY projects/ ./projects
WORKDIR projects/api
RUN uv build


FROM python:3.12
ARG wheel=api-0.1.0-py3-none-any.whl
RUN --mount=type=bind,from=build,source=/src/projects/api/dist/$wheel,target=$wheel \
    --mount=type=bind,from=build,source=/src/requirements.txt,target=requirements.txt \
    pip install --no-cache-dir -c requirements.txt $wheel
CMD ["uvicorn", "foo.api.core:app"]
