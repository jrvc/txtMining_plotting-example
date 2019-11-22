# txtMining_plotting-example
Simplified example for week5 of "Building Applications for NLP" course - autum 2019

This weeks assignment is meant to show you how to produce plots and display them in your website.

## Installation
Create a project directory:

```
mkdir myproject
cd myproject
```

(OPTIONAL) work in a virtual environment `myenv`:

```
python3 -m venv myenv
```
Install dependencies:
```
pip3 install -r requirements.txt
```

## Plotting


## Example in Flask

As in the previous session, we need to set some environment variables to show flask which file to run, enable development environment to activate interactive debugger and reloader, and set the port in which to run the application, e.g.:
```
export FLASK_APP=example.py
export FLASK_ENV=development
export FLASK_RUN_PORT=8800
```
And run it in Flask:
```
flask run
```
In your browser go to the URL `localhost:8800/search` and start using the tool.


