FROM python:3

WORKDIR /usr/src/app

COPY . .

# COPY requirements.txt ./
RUN pip install --no-cache-dir -r project/requirements.txt
RUN python project/db_create.py

EXPOSE 5000

CMD [ "python", "project/run.py" ]
