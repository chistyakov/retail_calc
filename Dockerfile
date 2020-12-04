FROM python:3.9.0-alpine3.12 as base
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
ENTRYPOINT ["./entrypoint.sh"]

FROM base as prod
COPY entrypoint.sh .
COPY retail_calc/src retail_calc/src

FROM base as dev
RUN apk add --no-cache --virtual .build-deps gcc musl-dev
COPY requirements-dev.txt ./
RUN pip install -r requirements-dev.txt
COPY . .
