#import flask framework
from flask import *


# below we create a web server based on application
app=Flask(__name__)



#Below we run the application

@app.route("/api/home")
def home():
  return jsonify ({"Message" :" Home route Accessed"})


    

@app.route("/api/products")
def products():
  return jsonify({"message":"Welcome to products route"})

# Below is route with addition
@app.route("/api/calc", methods=["POST"])
def calculator():
  if request.method=="POST":
    number1 = request.form["number1"]
    number2 = request.form["number2"]
    sum = float(number1)+ float(number2)
    return jsonify({"The answer is": sum})


#Assignment 01
# create a route that is able to calculate the simple interest given the pricipal as 20000, rate as 7% and time as 8 years.
@app.route("/api/interest", methods=["POST"])
def interest():
    if request.method=="POST":
     principal= request.form["principal"]
     rate = request.form["rate"]
     time = request.form["time"]
     simple_interest=int(principal)*int(time)*int(rate)/100
    return jsonify({"The simple interest":simple_interest})

app.run(debug=True)

#below we create home route
#routing : this is mapping /connecting different resources to differents functions


