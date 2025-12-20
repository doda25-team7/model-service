FROM python:3.11-slim
RUN pip install uv

ENV MODEL_PORT=8081

WORKDIR /app

COPY pyproject.toml .
COPY uv.lock .
COPY src ./src
COPY smsspamcollection ./smsspamcollection
RUN mkdir output
RUN uv run src/text_preprocessing.py
RUN uv run src/text_classification.py

EXPOSE 8081


CMD ["uv", "run", "src/serve_model.py"]
