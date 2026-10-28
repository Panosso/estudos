FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /data
ENV DB_PATH=/data/app.db
EXPOSE 3000
CMD ["python", "app.py"]

