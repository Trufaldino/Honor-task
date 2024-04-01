FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements_docker.txt

EXPOSE 80

CMD ["python3", "mail_app/main.py"]
