FROM python:3.7
COPY ./requirements.txt /
COPY src /frontend
RUN pip install -r /requirements.txt
ENV FLASK_APP=/frontend/main.py
CMD python -m flask run