rom flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

def ftoc(ftemp):
   return (ftemp-32.0)*(5.0/9.0)

def mtoKm(miles):
    return miles*1.609

@app.route('/ftoc/<ftempString>')
def convertFtoC(ftempString):
    ftemp = 0.0
    try:
        ftemp = float(ftempString)
        ctemp = ftoc(ftemp)
        return "In Farenheit: " + ftempString + " In Celsius " + str(ctemp) 
    except ValueError:
        return "Sorry.  Could not convert " + ftempString + " to a number"
@app.route('/mtoKm/<milesString>')
def convertmtoKM(milesString):
    miles = 0.0
    try:
        miles = float(milesString)
        kilometers = mtoKm(miles)
        return "In miles " + (milesString) + " In Kilometers " + str(kilometers)
    except ValueError:
        return "Sorry. Could not convert" + milesString + " to a number"
            

if __name__ == "__main__":
    app.run(port=5000)
