FROM alpine:latest
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
COPY N3/requirements.txt /usr/src/app
RUN pip install --nocache-dir -r /usr/src/app/requirements.txt

COPY N3/main.py /usr/src/app/

EXPOSE 5000

CMD ["python", "/usr/src/app/main.py"]

