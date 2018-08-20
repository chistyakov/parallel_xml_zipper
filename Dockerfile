FROM python:3.7-alpine


WORKDIR /xml_zipper


COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .


ENTRYPOINT ["./entrypoint.sh"]
