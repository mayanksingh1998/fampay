FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /fampay
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN
	touch /Users/mayanksingh/fampay/fampay.log

COPY . .

EXPOSE 8000