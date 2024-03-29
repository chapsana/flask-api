FROM python:3.10

ENV FLASK_APP run.py

COPY run.py gunicorn-cfg.py requirements.txt config.py .env ./
COPY app app
COPY migrations migrations

RUN pip install -r requirements.txt

EXPOSE 5005
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "run:app"]
