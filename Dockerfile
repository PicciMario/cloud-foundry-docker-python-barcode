FROM python:3.10-slim
RUN mkdir -p /app
WORKDIR /app
ADD barcode.py /app
RUN apt-get update && apt-get -y install zbar-tools poppler-utils
RUN apt-get clean
RUN pip install flask pyzbar pdf2image cfenv
EXPOSE 3333
CMD [ "python", "./barcode.py"]