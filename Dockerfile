FROM python:3.7-alpine

COPY bot /bot/

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bot

ENV TWEETPY_MODE main

CMD ["python3", "main.py", "${TWEETPY_MODE}"]