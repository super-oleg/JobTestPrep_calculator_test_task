JobTestPrep Calculator Challenge

## Description
This is a calculator that can perform basic arithmetic operations.
Using OOD/OOP principles.
## Getting Started
Standalone run server:
```commandline
pip install -r requirements.txt
python main.py
```
## Configuration
The server can be configured by creating the .env file.
The following variables are available:
* `HOST` - The port the server will listen on. Default is 0.0.0.0.
* `PORT` - The port the server will listen on. Default is 8000.
* `DEBUG` - The debug mode. Default is False.
* `TEMPLATE_DIR` - The directory where the templates are located. Default is 'templates'.
* `STATIC_DIR` - The directory where the static files are located. Default is 'static'.
### Dependencies
* Python 3.10
* requirements.txt
## Run containerized version
```commandline
docker build -t calculator_test . 
docker run -p 8000:8000 calculator_test
```