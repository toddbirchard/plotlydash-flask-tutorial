FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
VOLUME ["/usr/src/app"]
CMD [ "python", "./wsgi.py" ]