# Definition of Submission container

# We start from tensorflow-gpu image
FROM tensorflow/tensorflow:2.1.0-gpu-py3

# this line prevents interaction with tzdata package
ENV DEBIAN_FRONTEND=noninteractive
# from https://github.com/tensorflow/tensorflow/issues/10776
# this may not be needed if you use pytorch image
RUN cd /usr/local/cuda/lib64 \
    && mv stubs/libcuda.so ./ \
    && ln -s libcuda.so libcuda.so.1 \
    && ldconfig

# DO NOT MODIFY: your submission won't run if you do
RUN apt-get update -y && apt-get install -y --no-install-recommends \
         gcc \
         libsm6\
         libxext6\
         libxrender-dev\
         libc-dev\
         git \
         bzip2 \
         python-tk && \
     rm -rf /var/lib/apt/lists/*

# let's create our workspace, we don't want to clutter the container
RUN mkdir duckietown
COPY setup/requirementsnb.txt duckietown
WORKDIR duckietown
RUN pip install -r requirementsnb.txt

RUN pip list

RUN pip install -e git://github.com/AndreaCensi/zuper-nodes.git@z6#egg=zuper-nodes

COPY setup/launch_car_interface.sh .

RUN mkdir -p /data/config
RUN git clone https://github.com/duckietown/duckiefleet /data/config

COPY setup/solution.py .
COPY setup/modelname.h5 .
ADD setup/templates ./templates

#RUN ls
#RUN ls templates

# DO NOT MODIFY: your submission won't run if you do
ENV DUCKIETOWN_SERVER=evaluator

# let's see what you've got there...
CMD python3 solution.py
