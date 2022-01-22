#base image
FROM python
COPY . /Assignment
WORKDIR /Assignment
CMD python pyfile.py