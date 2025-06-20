FROM python:3.7

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install --no-cache-dir --no-deps -r requirements.txt

# port number
EXPOSE 8080

# write the command to run application
CMD ["python", "./application.py"]
