FROM alpine:latest
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache py3-pip
#RUN python3 -m ensurepip
COPY N3/requirements.txt /usr/src/app
RUN pip install -r /usr/src/app/requirements.txt

COPY N3/main.py /usr/src/app/

EXPOSE 5000

CMD ["python", "/usr/src/app/main.py"]

