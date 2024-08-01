# Serverless FastAPI on Azure 

Little project to tests Serverless FastAPI deployment on Azure. 

## Local run

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
$ pip install -r requirements-dev.txt

# Fire up local app server
$ uvicorn app.main:app --reload --log-level debug
```