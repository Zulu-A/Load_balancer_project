FROM python:3.11.5 as base

WORKDIR /application

RUN pip install flask

COPY ./server.py /application

ENTRYPOINT ["python", "/application/server.py"]

EXPOSE 5000