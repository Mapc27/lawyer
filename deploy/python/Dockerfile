FROM node:16-alpine AS node

WORKDIR /app

COPY src/web/static/vue/package.json .
COPY src/web/static/vue/package-lock.json .

RUN npm ci

COPY src/web/static/vue .

RUN npm run build


FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN pip install poetry==1.1.8 && poetry config virtualenvs.create false


WORKDIR /app
COPY pyproject.toml .
RUN poetry install --no-dev

COPY . .

COPY --from=node /app/dist /src/static/dist
#RUN python src/manage.py collectstatic --no-input

EXPOSE 8000

CMD python src/manage.py migrate && gunicorn --chdir src --bind 0.0.0.0:8000 lawyer.wsgi
