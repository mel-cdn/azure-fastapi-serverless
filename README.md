# Serverless FastAPI on Azure Function App

[![Build Status](https://github.com/mel-cdn/azure-fastapi-serverless/actions/workflows/deploy.yml/badge.svg?branch=main)](https://github.com/mel-cdn/azure-fastapi-serverless/actions/workflows/deploy.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Little project to explore Serverless FastAPI deployment on Azure.

With simple deployment workflow using GitHub Actions.

## Set up the project

```bash
# Clone project
$ git clone https://github.com/mel-cdn/azure-fastapi-serverless.git
$ cd azure-fastapi-serverless

# Install pipenv (environment manager)
$ pip install virtualenv

# Create and activate virtual environment (make sure you have python 3.11)
$ python -m virtualenv .venv
$ source venv/bin/activate 

# Install dependencies
$ pip install -r requirements.txt
$ pip install -r requirements-dev.txt
```

## Running locally using Azure Functions Core Tools

```bash
# Install via npm
# Alternative installation https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=linux%2Cbash%2Cazure-cli%2Cbrowser 
$ npm install -g azure-functions-core-tools@4

# Start local server
$ func start
```


## Testing the API
Using [Swagger Docs](https://demo-fastapi-serverless.azurewebsites.net/docs) or [Postman](https://www.postman.com/), you can test the deployed API of this project using below endpoints:

> If it's not working anymore, I probably ran out of Azure credits :)


- API Health
    ```bash
    GET https://demo-fastapi-serverless.azurewebsites.net

    Response:
    {
        "message": "API health at 100%."
    }
    ```

- Create User
    ```bash
    POST https://demo-fastapi-serverless.azurewebsites.net/users
    Body: {"userId": 1, "firstName": "Mel"}

    Response:
    {
      "userId": 1,
      "firstName": "Mel"
    }
    ```

- List Users
    ```bash
    GET https://demo-fastapi-serverless.azurewebsites.net/users

    Response:
    [
      {
        "userId": 1,
        "firstName": "Mel"
      }
    ]
    ```

- Get User
    ```bash
    GET https://demo-fastapi-serverless.azurewebsites.net/users/1

    Response:
    {
      "userId": 1,
      "firstName": "Mel"
    }
    ```

- Update User
    ```bash
    PUT https://demo-fastapi-serverless.azurewebsites.net/users/1
    Body: {"userId": 1, "firstName": "Mel Azure Updated", "lastName": "Cadano"}

    Response:
    {
      "userId": 1,
      "firstName": "Mel Azure Updated",
      "lastName": "Cadano"
    }
    ```

- Delete User
    ```bash
    DELETE https://demo-fastapi-serverless.azurewebsites.net/users/1

    Response:
    {
      "message": "OK"
    }
    ```

## Deploying your own service
> Create your Resource Group manually through Azure Portal and retrieve your login credentials.

```bash
# Install Azure CLI
$ curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Install Azure Functions Core Tools via npm
# Alternative installation https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=linux%2Cbash%2Cazure-cli%2Cbrowser
$ npm install -g azure-functions-core-tools@4

# Log in to Azure
$ az login \
  --service-principal \
  -t <tenant-id> \
  -u <client-id> \
  -p <client-secret>

# Create Storage Account where to store function files
$ az storage account create \
  --name <yourstorageaccount> \
  --resource-group <your-resource-group-rg> \
  --location japaneast \
  --sku Standard_LRS

# Create Function App
$ az functionapp create \
  --consumption-plan-location japaneast \
  --runtime python \
  --runtime-version 3.11 \
  --functions-version 4 \
  --name <your-function-app-name-fns> \
  --os-type linux \
  --resource-group <your-resource-group-rg> \
  --storage-account <yourstorageaccount>

# Publish Function App
$ func azure functionapp publish <your-function-app-name-fns>
```