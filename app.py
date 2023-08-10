from flask import Flask

##WSGI application
app = Flask(__name__)

## '@' decorator, comes along with the function, @app.route('url in string format')
@app.route('/')
def welcome():
    return "Congratulation Padma! you got selected in Microsoft with the package of 50LPA, you can on board immediately pls"


@app.route('/join')
def joining():
    return "please come and join us will give you the joining bonus of 10 LPA"

#like this we can create any number of urls.

if __name__=="__main__":
    app.run(debug=True)