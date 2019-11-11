FROM python:3.7

RUN apt-get update -y
WORKDIR /app
RUN pip install flask gunicorn
COPY . /app
RUN pip install -r requirements.txt

EXPOSE 8000
CMD [ "gunicorn", "-b", "0.0.0.0:8000", "run:app" ]