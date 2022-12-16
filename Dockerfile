FROM python:3.10.8

ENV PYTHONUNBUFFERED = value

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000