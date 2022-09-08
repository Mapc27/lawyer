FROM python:3.10

RUN pip install poetry==1.1.8 && \
    poetry config virtualenvs.create false

ENV PYTHONUNBUFFERED 1

WORKDIR /app/

COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install

COPY . .

RUN python src/manage.py collectstatic --no-input

EXPOSE 8000

CMD python src/manage.py migrate && python src/manage.py runserver 0.0.0.0:8000
