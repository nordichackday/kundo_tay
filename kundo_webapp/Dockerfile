FROM kundo_torch_env

USER root

RUN apt-get -y update \
	&& apt-get install -y nginx python python-pip python-dev \
	&& pip install Flask==0.10.1 && pip install gunicorn \
    flask-cors

# Setup flask app
RUN mkdir -p /app
ADD app /app

# Deploy start script
ADD start /usr/local/bin/start
RUN chmod +x /usr/local/bin/start

CMD /usr/local/bin/start
