FROM python:3.7
COPY ./requirements.txt /
COPY ./src /store
RUN pip install -r /requirements.txt
ENV FLASK_APP=/store/main.py
CMD python -m flask run