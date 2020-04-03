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