FROM python:3.10-slim
RUN mkdir -p /app
WORKDIR /app
RUN apt-get update && apt-get -y install zbar-tools poppler-utils
RUN apt-get clean
RUN pip install flask pyzbar pdf2image cfenv sap-xssec
ADD barcode.py /app
EXPOSE 3333
CMD [ "python", "./barcode.py"]