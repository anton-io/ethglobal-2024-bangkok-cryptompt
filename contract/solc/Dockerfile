# This docker container provides the necessary tools to compile smarts-contracts.
FROM --platform=linux/amd64 ubuntu:24.04 as solc
MAINTAINER Antonio Roldao <docker@anton.io>

ARG VERSION=0.0.1

LABEL name="solc" version=$VERSION

ENV DEBIAN_FRONTEND=noninteractive
ENV DOCKER_DEFAULT_PLATFORM=linux/amd64

# Install core components.
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install software-properties-common

# Install npm.
RUN apt-get -y install npm

# Install solc.
RUN add-apt-repository ppa:ethereum/ethereum -y && \
    apt-get update && \
    apt-get install solc

# Install typical contract dependencies.
RUN npm i -g "@openzeppelin/contracts"
RUN npm i -g "@flarenetwork/flare-periphery-contracts"
RUN npm i -g "@chainlink/contracts"

# Allow the selection of the solc version.
RUN apt-get -y install python3-pip
RUN pip3 install solc-select --break-system-packages
RUN solc-select use 0.8.19 --always-install

# Configure entry point with option to run bash.
WORKDIR /root
COPY entrypoint.sh entrypoint.sh
RUN chmod u+x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]