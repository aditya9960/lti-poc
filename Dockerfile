 FROM aaditya/python-2.7
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /lti-poc
 WORKDIR /lti-poc
 COPY . /lti-poc
 RUN rm -rf migrations
 RUN apt-get -y update --fix-missing
 RUN apt-get -y install curl wget make gcc build-essential --fix-missing
 ADD requirements.txt /lti-poc/
 RUN pip install -r requirements.txt
 ADD . /lti-poc/
 ADD /docker-entrypoint-initdb.d/init.sql /docker-entrypoint-initdb.d/
 RUN chmod u+x docker-entrypoint.sh
 ENTRYPOINT ["bash", "/lti-poc/docker-entrypoint.sh"]
