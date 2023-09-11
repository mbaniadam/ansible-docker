FROM alpine:latest
RUN apk add --update --no-cache py3-pip gcc python3-dev build-base linux-headers
COPY App-Get-Metrics/requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
COPY App-Get-Metrics/main.py /usr/src/app/

EXPOSE 5000

CMD ["python","/usr/src/app/main.py"]