FROM ubuntu:20.04 
FROM python:3.8.5

WORKDIR /server

RUN python -m venv /opt/venv

COPY requirements.txt .

RUN . /opt/venv/bin/activate && pip install -r requirements.txt

COPY app.py .

CMD . /opt/venv/bin/activate && exec python myapp.py
