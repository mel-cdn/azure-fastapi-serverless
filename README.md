# Serverless FastAPI on Azure

Little project to tests Serverless FastAPI deployment on Azure.

## Setup the project

```bash
# Clone project
$ git clone https://github.com/mel-cdn/az-fastapi-serverless.git
$ cd az-fastapi-serverless

# Install pipenv (environment manager)
$ pip install virtualenv

# Create virtual environment (make sure you have python 3.11)
$ virtualenv venv

# Install dependencies
$ pip install -r requirements.txt
```

## Running locally using Uvicorn

```bash
$ uvicorn app.main:app --reload --log-level debug
```

## Running locally using Azure Functions Core Tools

```bash
# Install tools via npm
$ npm install -g azure-functions-core-tools@3

# Start local server
$ func start
```
