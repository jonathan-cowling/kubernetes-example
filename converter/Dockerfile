FROM python:3.7
COPY ./requirements.txt /
COPY src /app
RUN pip install -r /requirements.txt
ENV FLASK_APP=/app/main.py
EXPOSE 5000
CMD python -m flask run --host=192.168.1.1 --port 5000