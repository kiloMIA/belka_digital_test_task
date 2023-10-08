FROM python:3.10 AS build

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

FROM python:3.10-slim

WORKDIR /app

COPY --from=build /app/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY --from=build /app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7777"]