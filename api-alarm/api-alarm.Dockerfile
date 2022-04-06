FROM python:3.8.3-slim

COPY ./api-alarm/requirements.txt /api-alarm/requirements.txt
COPY ./api-alarm/sources /api-alarm
WORKDIR /api-alarm

RUN pip3 install -r /api-alarm/requirements.txt

# e.g ENTRYPOINT ["python3" "sample.py"]
#     ENTRYPOINT ["gunicorn" "sample:app"]
ENTRYPOINT [""]
