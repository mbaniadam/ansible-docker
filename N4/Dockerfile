FROM alpine:latest
RUN apk add --update --no-cache py3-pip gcc python3-dev
COPY N3/requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
COPY N3/main.py /usr/src/app/

EXPOSE 5000

CMD ["python","/usr/src/app/main.py"]