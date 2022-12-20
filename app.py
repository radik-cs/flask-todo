from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_MODIFICATIONS'] = False
db = SQLAlchemy(app)



@app.route('/')
def index():
    return render_template('base.html')


@app.route('/about')
def about():
    return "About"


 
    if __name__ =="__main__":
        db.create_all()
        app.run(debuf=True)