FROM python:3.7-alpine

RUN apk add --update --no-cache g++ gcc libxslt-dev

WORKDIR /xml_zipper


COPY requirements.txt ./
COPY test-requirements.txt ./
RUN pip install -r requirements.txt -r test-requirements.txt

ENV ZIP_COUNT 50
ENV XML_COUNT 100

ENV MIN_LEVEL 1
ENV MAX_LEVEL 100

ENV LENGTH_OBJECT_NAME 5

ENV MIN_OBJECTS_COUNT 1
ENV MAX_OBJECTS_COUNT 10

ENV LEVELS_FILENAME levels.csv
ENV NAMES_FILENAME object_names.csv

COPY . .

ENTRYPOINT ["./entrypoint.sh"]
