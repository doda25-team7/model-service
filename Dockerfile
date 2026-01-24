FROM python:3.11-slim
RUN pip install uv==0.9.22

ENV MODEL_PORT=8081

WORKDIR /app

COPY pyproject.toml .
COPY uv.lock .
COPY src ./src
RUN mkdir data
RUN uv sync --locked

EXPOSE 8081


CMD ["uv", "run", "src/serve_model.py"]
