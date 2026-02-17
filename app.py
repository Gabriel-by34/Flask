#import flask framework
from flask import*


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
  if request.method==["POST"]:
    number1=request.form["number1"]
    number2=request.form["number2"]
    sum=int(number1)+int(number2)
    return jsonify({"The answer is" :sum})



app.run(debug=True)

#below we create home route
#routing : this is mapping /connecting different resources to differents functions


