# April-Fool-Prank-App

It's a simple web-app create using AWS Elastic Beanstalk. It's based on flask and uses Bootstrap CSS. 

Application link - https://bit.ly/2Jn9ra1

## Motivation
The idea of was simple to create an application were put info to get H1B lottery result, which was supposed to be out by 31st March. I liked the app because it took me just an hour to deploy this application. 

## Getting Started 
To follow the procedures in this guide, please have following installed:
- Python 3.8
- Elastic Beanstalk Command Line Interface (EB CLI): https://github.com/aws/aws-elastic-beanstalk-cli-setup

## Steps to Create Application 
These steps are heavily borrowed from tutorial given on AWS webiste:

- Create Project Directory 
```
~$ mkdir eb-flask
~$ cd eb-flask
```

- Create and activate a virtual environment named virt:
```
~/eb-flask$ virtualenv virt
~$ source virt/bin/activate
```

- Install flask with pip install
```
(virt)~/eb-flask$ pip install flask
```

- Save the output from pip freeze to a file named requirements.txt
```
(virt)~/eb-flask$ pip freeze > requirements.txt
```

- Create Flask application 
In this step, I used two simple html pages (fool.html and index.html). Further, I have used Bootstrap CSS framework to minimise to make the design look a big elegant. 

All the routing code is in application.py. It's pretty simple. 
```
from flask import Flask, render_template, request, redirect, url_for, jsonify

application = Flask(__name__)

@application.route('/')
def index():
    action = request.args.get('submit_button')
    if action!=None:
        return render_template('fool.html')
    return render_template('index.html')

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
```

- Run application.py with Python:
```
(virt) ~/eb-flask$ python application.py
```

- Add an .ebignore file that tells the EB CLI to leave out the virt folder
```
virt
```
- Initialize your EB CLI repository with the eb init command:
```
~/eb-flask$ eb init -p python-3.6 flask-tutorial --region us-east-2
```

- Create an environment and deploy your application to it with eb create
```
~/eb-flask$ eb create flask-env
```

- To open the website
```
~/eb-flask$ eb open
```

- Deploy a new version of webite after making changes 
```
eb deploy
```