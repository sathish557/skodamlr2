

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))
''' 
# creating an evnironment variable and set this to dev
ENV = 'dev'
#if env== dev  we have our database (skoda), else we have production db

if ENV == 'dev':
    app.debug=True   # setting debug in development mode
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:asdf1234@localhost/skoda'                           
     # we set up our development database
     # postgres is what you select when creating skoda database and password as usual

else:
    app.debug=False  # production mode debug off
    app.config['SQLALCHEMY_DATABASE_URI'] = ''



app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # if not we get error

db = SQLAlchemy(app)  # the way sqlalchemy works is we create models, so create model now using class

class firstclass(db.Model): # extends to database model
    __tablename__ = 'skoda_table' # define table name
    id = db.Column(db.Integer, primary_key=True) # define variables
    HP = db.Column(db.Integer)
    VOL = db.Column(db.Integer)
    SP = db.Column(db.Integer)
    WT = db.Column(db.Integer)
 #   output = db.column(db.Integer)

    def __init__(self,HP, VOL, SP, WT): # creating a constructor with all variables except id
        self.HP = HP
        self.VOL = VOL
        self.SP = SP
        self.WT = WT
    #    self.output = output  '''


## now run this file
# and run the commands in python terminal
# from  mlr_app import db
# db.create_all()



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predicting():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
        
    output = round(prediction[0],2)
    return render_template('success.html',prediction_text = 'Predicted Mileage of this Car is --->  {}  Miles/Gallon'.format(output)) 
    


'''     HP = request.form['HP']
    VOL = request.form['VOL']
    SP = request.form['SP']
    WT = request.form['WT']
    

    data = firstclass(HP, VOL, SP, WT,output) # we are creating data for server from class (model) firstclass
    db.session.add(data)
    db.session.commit()

 '''
     
  


if __name__ == '__main__':
    app.run()
    # take off debug option as we are going to prodution mode
    
