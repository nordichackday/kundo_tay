FROM ubuntu:14.04

RUN apt-get -y update

# Setup python
RUN apt-get -y install \
	python2.7-dev \
	libhdf5-dev \
	python-pip \
	git

RUN pip install virtualenv
RUN mkdir /app && chown daemon:daemon /app

WORKDIR /app
USER daemon

RUN git clone https://github.com/jcjohnson/torch-rnn.git
RUN virtualenv .env
RUN . .env/bin/activate \
	&& cd torch-rnn \
	&& pip install -r requirements.txt

# Setup torch
RUN git clone https://github.com/torch/distro.git torch --recursive
USER root
RUN apt-get -y install software-properties-common python-software-properties
RUN cd torch && sed 's/sudo //' -i install-deps && bash install-deps
USER daemon
RUN cd torch && ./install.sh
USER root
RUN . /app/torch/install/bin/torch-activate \
	&& luarocks install torch \
	&& luarocks install nn \
	&& luarocks install optim \
	&& luarocks install lua-cjson

USER daemon
RUN git clone https://github.com/deepmind/torch-hdf5
USER root
RUN cd torch-hdf5 \
	&& . /app/torch/install/bin/torch-activate \
	&& luarocks make hdf5-0-0.rockspec

USER daemon
WORKDIR /app/torch-rnn

# content from torch-activate
ENV LUA_PATH='/usr/sbin/.luarocks/share/lua/5.1/?.lua;/usr/sbin/.luarocks/share/lua/5.1/?/init.lua;/app/torch/install/share/lua/5.1/?.lua;/app/torch/install/share/lua/5.1/?/init.lua;./?.lua;/app/torch/install/share/luajit-2.1.0-beta1/?.lua;/usr/local/share/lua/5.1/?.lua;/usr/local/share/lua/5.1/?/init.lua'
ENV LUA_CPATH='/usr/sbin/.luarocks/lib/lua/5.1/?.so;/app/torch/install/lib/lua/5.1/?.so;./?.so;/usr/local/lib/lua/5.1/?.so;/usr/local/lib/lua/5.1/loadall.so'
ENV PATH=/app/torch/install/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV LD_LIBRARY_PATH=/app/torch/install/lib:$LD_LIBRARY_PATH
ENV DYLD_LIBRARY_PATH=/app/torch/install/lib:$DYLD_LIBRARY_PATH
ENV LUA_CPATH='/app/torch/install/lib/?.so;'$LUA_CPATH

ADD file.t7 /data/file.t7
ADD file.json /data/file.json
