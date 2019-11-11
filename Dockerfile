FROM python:3

WORKDIR /app

COPY gunicorn_app/requirements.txt ./
RUN pip install -r requirements.txt

COPY gunicorn_app /app
EXPOSE 8080
CMD [ "gunicorn", "-b", "127.0.0.1:8000", "/run.py" ]