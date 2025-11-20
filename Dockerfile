FROM python:3.11-slim

ENV MODEL_PORT=8081

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src ./src

COPY output ./output

EXPOSE 8081

CMD ["python", "src/serve_model.py"]