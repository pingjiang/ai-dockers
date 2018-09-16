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

RUN pip install -r /ai_server/requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "/ai_server/app.py"]
