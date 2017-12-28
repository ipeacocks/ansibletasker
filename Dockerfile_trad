FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r project/requirements.txt && python project/db_create.py

EXPOSE 5000

CMD [ "python", "project/run.py" ]
