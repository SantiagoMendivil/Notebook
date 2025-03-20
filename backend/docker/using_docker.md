# Table of contents 
- [Table of contents](#table-of-contents)
- [Using Docker](#using-docker)
  - [Build the container](#build-the-container)
  - [Run the container](#run-the-container)

# Using Docker
You have to have installed the Docker Desktop application in order to manage, create, run and delete docker containers in you computer.

## Build the container
Once you have a repository on github, for example a React application, you have to run: 

```shell 
docker build -t directory_name .
```

Where the t flag tags your image with a name. And the dot (.) lets Docker know where it can find the Dockerfile.
Once the command is run in the shell of your IDE it will start building the container. 

This works if the **Dockerfile** already exists in the repository.

## Run the container
Once the build is complete, an image will appear in the Images tab within the Docker icon in the IDE you're working on. 

You can then select the image name to see its details. Then select **Run** to run it as a container. In the optional settings specify the port number to run this container. 