# Serverless FastAPI on Azure

Little project to explore Serverless FastAPI deployment on Azure.

With simple deployment workflow using GitHub Actions.

## Set up the project

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

## Running locally using Azure Functions Core Tools

```bash
# Install tools via npm
$ npm install -g azure-functions-core-tools@3

# Start local server
$ func start
```

## Deploying using Azure CLI
```bash

# Install Azure CLI
$ curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Log in to Azure
$ az login --service-principal -u ${{ secrets.AZURE_CREDENTIALS }}

# Deploy to Azure Functions
$ az functionapp deployment source config-zip \
  --resource-group <your-resource-group> \
  --name ${{ secrets.AZURE_FUNCTIONAPP_NAME }} \
  --src function_app.zip

# Cleanup
$ rm function_app.zip
```

## Testing the API
Using [Postman](https://www.postman.com/) or similar, you can test the deployed API of this project using below endpoints:

> If it's not working anymore, I probably ran out of Azure credits :)


- API Health
    ```bash
    GET https://az-fastapi-serverless.azurewebsites.net

    Response:
    {
        "message": "API health at 100%."
    }
    ```

- Create User
    ```bash
    POST https://az-fastapi-serverless.azurewebsites.net/users
    Body: {"userId": 1, "firstName": "Mel"}

    Response:
    {
      "userId": 1,
      "firstName": "Mel"
    }
    ```

- List Users
    ```bash
    GET https://az-fastapi-serverless.azurewebsites.net/users

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
    GET https://az-fastapi-serverless.azurewebsites.net/users/1

    Response:
    {
      "userId": 1,
      "firstName": "Mel"
    }
    ```

- Update User
    ```bash
    PUT https://az-fastapi-serverless.azurewebsites.net/users/1
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
    DELETE https://az-fastapi-serverless.azurewebsites.net/users/1

    Response:
    {
      "message": "OK"
    }
    ```
