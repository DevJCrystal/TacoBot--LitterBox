from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

isRunning = "F"

f = open("motor.txt", "r")
isRunning = f.read()
f.close()

@app.route('/')
def homepage():
    global isRunning
    Message = None

    print(isRunning)
    if (isRunning == "E"):
        Message = "LitterBox in Error State!"
    else:
        Message = ""

    return render_template('home.html', motorRunning=isRunning, Message=Message)

@app.route('/run')
def background_process_test():
    global isRunning

    # This is to prevent running if there was a loss of power.
    # Will need to be reset.
    if (isRunning != "E"):
        isRunning = "T"
        print ("Run Litter Cleanup")
        f = open("motor.txt", "w")
        f.write(isRunning)
        f.close()
    return redirect(url_for('homepage'))

if __name__ == '__main__':
    app.run(host="0.0.0.0")