FROM python:3.6 

LABEL maintainer="pingjiang"

# clone latest dlib
ENV DLIB_VERSION="19.15"

RUN apt-get update

RUN apt-get -y install libopenblas-dev liblapack-dev build-essential \
    cmake \
    git \
    wget \
    unzip \
    yasm \
    pkg-config \
    libopencv-dev \
    python-opencv \
    libswscale-dev \
    libtbb2 \
    libtbb-dev \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libavformat-dev \
    libpq-dev

COPY thirdparty /thirdparty/

# RUN wget http://dlib.net/files/dlib-${DLIB_VERSION}.tar.bz2
RUN tar xvf /thirdparty/dlib-${DLIB_VERSION}.tar.bz2
RUN mkdir /dlib-${DLIB_VERSION}/build
WORKDIR /dlib-${DLIB_VERSION}/build 
RUN cmake .. && cmake --build . --config Release
RUN make install && ldconfig

WORKDIR /dlib-${DLIB_VERSION}
RUN pkg-config --libs --cflags dlib-1
RUN python setup.py install
RUN rm -rf /dlib-${DLIB_VERSION}.tar.bz2
RUN rm -rf /dlib-${DLIB_VERSION}

# clean up all temporary files 
RUN apt-get clean &&\
    apt-get autoclean -y &&\
    apt-get autoremove -y &&\
    apt-get clean &&\
    rm -rf /tmp/* /var/tmp/* &&\
    rm -rf /var/lib/apt/lists/* &&\    
    rm -f /etc/ssh/ssh_host_*

COPY *.py requirements.txt /ai_server/
COPY handlers /ai_server/handlers/
COPY models /ai_server/models/
COPY utils /ai_server/utils/
COPY tools /ai_server/tools

WORKDIR /ai_server/tools/matting
RUN make

RUN mkdir -p /ai_server/bin/; mv matting /ai_server/bin/

RUN chmod +x /ai_server/bin/*

WORKDIR /

# http://mirrors.aliyun.com/pypi/simple/
RUN pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -r /ai_server/requirements.txt
RUN pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com uwsgi

EXPOSE 80

# -H ~/.venv/py3/
ENTRYPOINT uwsgi --http :80 --wsgi-file /ai_server/app.py --enable-threads --master
