FROM python
WORKDIR /app
RUN mkdir /database
COPY ./app/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY ./app/main.py /app/main.py
RUN apt-get update
RUN apt-get install sqlite3
CMD ["python", "/app/main.py"]
