FROM python:3

# set a directory for the app
WORKDIR /Users/huntermitchell/Documents/PYTHON_FILES/webApp/app

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install --no-cache-dir --no-deps -r requirements.txt

# port number
EXPOSE 5000

# write the command to run application
CMD ["python", "./application.py"]
