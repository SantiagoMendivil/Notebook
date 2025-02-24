# Table of contents
- [Table of contents](#table-of-contents)
- [Containerizing the app using Docker](#containerizing-the-app-using-docker)
  - [How it works](#how-it-works)
  - [Steps](#steps)

# Containerizing the app using Docker 
Docker is a powerful tool that makes it easy to run applications regardless of the machine you wrote the code on and the machine you want to run it on. It is widely used in practice as it allows developers to avoid the “But it runs on my laptop!” problem when their code doesn’t work. 

## How it works 
1. Create a requirements.txt file
2. Set allowed hosts to * 
3. Create a Dockerfile which contains instructions on how to buid a Docker image
4. Run docker compose up to create a container image and run it 
5. Commit and push the image to a remote repo so others can run it exactly as you've configured.

## Steps 
- Create the requirements file
- Create the Dockerfile
```docker
# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

Explanation of this file:
- `# syntax=docker/dockerfile:1`: Specifies the syntax version for the Dockerfile.
- `FROM python:3`: Uses the official Python 3 image as the base image.
- `ENV PYTHONDONTWRITEBYTECODE=1`: Prevents Python from writing .pyc files to disk.
- `ENV PYTHONUNBUFFERED=1`: Ensures that the Python output is sent straight to the terminal without being buffered.
- `WORKDIR /code`: Sets the working directory inside the container to `/code`.
- `COPY requirements.txt /code/`: Copies the `requirements.txt` file from the host to the `/code/` directory in the container.
- `RUN pip install -r requirements.txt`: Installs the Python dependencies listed in `requirements.txt`.
- `COPY . /code/`: Copies the entire project directory from the host to the `/code/` directory in the container.
- `CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]`: Specifies the command to run the Django development server on port 8000.
The `FROM` line indicates what base container image we want to build on. 
- Run the following command 
```bash 
docker build . -t my-django-app:latest && docker run -e PYTHONUNBUFFERED=1 -p  8000:8000 my-django-app 
```