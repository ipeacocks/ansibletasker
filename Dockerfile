FROM alpine:3.7

RUN apk add --update \
    python3 \
    python3-dev \
    build-base \
    libffi-dev \
    openssl-dev \
  && rm -rf /var/cache/apk/*

WORKDIR /app

COPY . .
RUN pip3 install --no-cache-dir -r project/requirements.txt
RUN python3 project/db_create.py

EXPOSE 5000
CMD ["python3", "project/run.py"]