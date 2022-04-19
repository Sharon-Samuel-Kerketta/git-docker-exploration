FROM continuumio/miniconda3:4.10.3-alpine

WORKDIR /app

COPY . .

ARG TEST_ARGS
ARG TE=$TEST_ARGS

RUN echo ${TE} > testing.txt;

# RUN ./test.sh

RUN pip install -r requirements.txt
