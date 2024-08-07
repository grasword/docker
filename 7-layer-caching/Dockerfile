FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN apt-get update && \
    apt-get install -y \
    curl \
    wget \
    vim

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "app.py"]

### Optimized Dockerfile

FROM python:3.9-slim
WORKDIR /app

COPY requirements.txt /app/
RUN apt-get update && \
    apt-get install -y \
    curl \
    wget \
    vim && \
    pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["python", "app.py"]