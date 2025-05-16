FROM python:3-slim-buster
RUN apt-get update && \
    apt-get install -y wget curl build-essential libssl-dev libffi-dev python3-dev && \
    pip install --upgrade setuptools wheel && \
    pip install requests favicon
COPY download_favicon.py /usr/src/app/download_favicon.py
WORKDIR /usr/src/app
ENTRYPOINT ["python", "/usr/src/app/download_favicon.py"]
