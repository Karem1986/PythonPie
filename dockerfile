# Importing the base image, since our application is in Python we will use the Python image.
FROM python:latest

# Specify where to copy the files to in the container in Docker
WORKDIR /opt/app

# Import python code into the image, / means that the code will be at the image root folder
COPY main.py /

# Command to execute to run the image pie-python from the container
CMD [ "python", "./main.py"]

# Command that will run durint the image building process
RUN python3 

# Map it to a port
EXPOSE 6070:80
