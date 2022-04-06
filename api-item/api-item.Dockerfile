FROM python:3.8.3-slim

COPY ./api-item/requirements.txt /api-item/requirements.txt
COPY ./api-item/sources /api-item
WORKDIR /api-item

RUN pip3 install -r /api-item/requirements.txt

# e.g ENTRYPOINT ["python3" "sample.py"]
#     ENTRYPOINT ["gunicorn" "sample:app"]
ENTRYPOINT [""]
