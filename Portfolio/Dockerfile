
# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.11

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

RUN apt-get install -y python3


# Set the working directory to /music_service
WORKDIR /Portfolio
COPY requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt

RUN pip3 install -r requirements.txt
COPY . .





