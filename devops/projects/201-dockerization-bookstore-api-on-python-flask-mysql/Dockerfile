FROM ubuntu:20.04
RUN apt-get update -y && apt-get install python3 python3-pip -y
COPY requirements.txt .
RUN pip3 install -r ./requirements.txt
COPY bookstore-api.py .
EXPOSE 5000
CMD ["python3", "bookstore-api.py"]