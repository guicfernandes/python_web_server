# python_web_server
A Python project to study how to build a web server in python

## Installation 
### Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

Linux
```bash
mkdir myproject
cd myproject
python3 -m venv venv
. venv/bin/activate
pip install Flask
```

Windows
```cmd
mkdir myproject
cd myproject
py -3 -m venv venv
venv\Scripts\activate
pip install Flask
```

## Usage

Linux
```bash
export FLASK_APP=server
export FLASK_ENV=development
flask run
```
Windows
```cmd
set FLASK_APP=hello
set FLASK_ENV=development
flask run
```

# Referencies
[Flask Documentation](https://flask.palletsprojects.com/en/2.1.x/)

[Complete Python Developer - Zero to Mastery](https://zerotomastery.io/courses/learn-python/)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Guilherme's GitHub](https://github.com/guicfernandes/)