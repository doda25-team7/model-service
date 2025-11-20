FROM python:3.11-slim
COPY --from=ghcr.io/astral-sh/uv:0.9.10 /uv /uvx /bin/

ENV MODEL_PORT=8081

WORKDIR /app

COPY pyproject.toml .
COPY uv.lock .
COPY src ./src
RUN uv sync --locked

COPY output ./output

EXPOSE 8081


CMD ["uv", "run", "src/serve_model.py"]