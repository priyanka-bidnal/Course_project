FROM python:3.12-slim
WORKDIR /online
COPY . .
CMD ["python","online.py"]
