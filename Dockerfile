FROM ubuntu:14.04

RUN mkdir /udadisi-twitter
ADD . /udadisi-twitter
RUN chmod -R 755 /udadisi-twitter
WORKDIR /udadisi-twitter

RUN apt-get update
RUN apt-get install -y python python-dev python-pip
RUN pip install -r requirements.txt
RUN python -m nltk.downloader stopwords
EXPOSE 5000
CMD python application.py