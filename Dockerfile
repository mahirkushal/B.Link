FROM python:3.8.7-buster
#ADD . /

WORKDIR /code
ENV FLASK_APP=TaskA.py
ENV FLASK_RUN_HOST=0.0.0.0
#RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt .

RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]