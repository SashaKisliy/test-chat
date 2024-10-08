## Installing using GitHub
Before you begin, ensure you have met the following requirements:
Docker must be already installed for running the server with docker-compose.
Python3 must be already installed.
Run the project locally without Docker
Clone the repository:

```shell
git clone https://github.com/SashaKisliy/test-chat.git
```
#### Go to the project directory:
```shell
cd theatre_api
```
#### Create a virtual Python environment and activate it:
```shell
python -m venv .venv 
source .venv/bin/activate   # on macOS
.\.venv\Scripts\activate    # on Windows
```
#### Set the project dependencies:
```shell
pip install -r requirements.txt
```
## Environment Setup

To configure the project, create a .env file in the root directory of your project
and add the following variables or check .env.sample file:

```dotenv
DEBUG=True
SECRET_KEY=your-secret-key
```

## Starting the server
1. Create database migrations:
```shell
python manage.py migrate
```
2. Create a superuser for accessing the admin interface:
```shell
python manage.py createsuperuser
```
3. Start the development server:
```shell
python manage.py runserver
```
The API should now be accessible at http://localhost:8080/


## Run with Docker
Docker should be installed

```shell
docker-compose build
docker-compose up
```
The API should now be accessible at http://localhost:8081/



