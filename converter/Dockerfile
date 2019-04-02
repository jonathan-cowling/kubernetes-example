FROM python:3.7
COPY ./requirements.txt /
COPY ./src /converter
RUN pip install -r /requirements.txt
ENV FLASK_APP=/converter/main.py
CMD python -m flask run