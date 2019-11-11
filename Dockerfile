FROM python:3.7

RUN apt-get update -y
RUN apt-get install postgres
WORKDIR /app
RUN pip install flask gunicorn
COPY . /app
RUN pip install -r requirements.txt
RUN postgres -p 8000

EXPOSE 8080
CMD [ "gunicorn", "-b", "127.0.0.1:8000", "/run.py" ]