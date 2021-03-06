FROM python:3.7-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apk add build-base
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./app /service/app
WORKDIR /service

ENTRYPOINT ["python", "-m", "app"]