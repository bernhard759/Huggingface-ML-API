# Huggingface-ML-API


## Overview

This project demonstrates how to deploy a machine learning API using FastAPI, Docker, and AWS Lightsail. The API utilizes a Hugging Face Transformer model to classify documents and images, providing a robust solution for serving machine learning models as web services.

## Tech Stack

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **Docker**: An open-source containerization platform that packages applications into containers.
- **Docker Compose**: A tool for defining and running multi-container Docker applications.
- **AWS Lightsail**: A simplified cloud platform that offers everything needed to deploy, manage, and scale applications.

## Project Structure

```plaintext
├── app.py
├── docker-compose.yml
├── Dockerfile
├── download.py
├── LICENSE
├── README.md
├── requirements.txt
└── utils.py
```

### app.py

This file contains the core source code for building and running the FastAPI application with three endpoints:

- **GET `/`**: The homepage.
- **POST `/document-classifier`**: Takes a PDF file as input and returns a JSON response with the document's classification.
- **POST `/classify-image`**: Takes an image file as input and returns a JSON response with the image's classification.

### docker-compose.yml

A configuration file for Docker Compose to deploy, combine, and configure multiple Docker containers simultaneously.

### Dockerfile

The Dockerfile includes all commands needed to build and run the Docker image.

### download.py

This file downloads the pre-trained model from Hugging Face.

### requirements.txt

Contains the necessary requirements for the API.

### utils.py

Includes functions that generate the classifications for PDF and image files.

## How to Run the API

To build and run the application using Docker Compose, execute the following command in your terminal:

```sh
docker-compose up -d --build
```

## Credits

This project is based on the tutorial by Ifeanyi Nneji, published in "AWS in Plain English". For more details, refer to the original article: [How to Deploy a Machine Learning API on AWS Lightsail](https://aws.plainenglish.io/how-to-deploy-a-machine-learning-api-on-aws-lightsail-151052470b7d).
