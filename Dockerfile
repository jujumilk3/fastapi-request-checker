FROM python:3.10-slim-buster
WORKDIR /app
ENV PYTHONPATH=/app

RUN apt-get update && apt-get install vim -y; \
    rm -rf /var/lib/apt/lists/*;

COPY poetry.lock pyproject.toml /app/
RUN pip install poetry
RUN poetry install -n -v && rm -r --interactive=never ~/.cache/pypoetry/cache ~/.cache/pypoetry/artifacts
RUN pip cache purge

COPY main.py /app/

EXPOSE 80
CMD poetry run uvicorn main:app --host 0.0.0.0 --port 80 --reload