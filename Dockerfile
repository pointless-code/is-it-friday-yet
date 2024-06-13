FROM python:3.9-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install pytz

CMD ["python", "./check_day.py"]
