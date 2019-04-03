FROM python:3.7
COPY ./requirements.txt /
COPY src /app
RUN pip install -r /requirements.txt
ENV FLASK_APP=/app/main.py
EXPOSE 5001
CMD python -m flask run --host=0.0.0.0 --port 5001