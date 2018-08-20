FROM python:3.7-alpine


WORKDIR /xml_zipper


COPY requirements.txt ./
COPY test-requirements.txt ./
RUN pip install -r requirements.txt -r test-requirements.txt
COPY . .


ENTRYPOINT ["./entrypoint.sh"]
