from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return 'Dojo!'

#Create a route that responds with "Hi" and whatever name is in the URL after /say/
@app.route('/say/<string:name>')
def say_hello(name):
    print(name)
    return (f"Hi there, {name}!")

#Create a route that responds with the given word repeated as many times as specified in the URL
@app.route('/say/<string:name>/<int:num>')
def repeat_name(name, num):
    print(name)
    print(num)
    return (f"Hi there, {name * num}!")

#Ensure that if the user types in any route other than the ones specified, they receive an error message saying "Sorry! No response. Try again." AKA custom error handling in Flask
@app.errorhandler(404) 
def invalid_route(e): 
    return "Sorry! No response, try again!"



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
