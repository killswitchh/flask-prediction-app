FROM python:3.8.5-alpine3.11
WORKDIR /code
ADD . /code
RUN pip install -r requirements.txt
CMD ["python","app.py"]