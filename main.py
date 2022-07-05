# integrating the html page in the flask app using library like render_template
import math
from flask import Flask,redirect,url_for,render_template,request # the request is used to read the posted values
app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/result/<float:per>')
def result(per):
    
    return  render_template('result.html',percen=per)


@app.route('/fail/<int:score>')
def fail(score):
    if score < 35:
        return "oh! you are failed the exam better luck next time and u got !!!!" + str(score)
    else:
        return "u are passed go to the success page"


@app.route('/results/<int:marks>')
def results(marks):
    results=''
    if marks < 35:
        results='fail'
    else:
        results='pass'
    return redirect(url_for(results,marks=marks))


# from this we will take the inputs from the user using the html page
@app.route('/submit/',methods=['POST','GET'])
def submit(): # this submit function will pick up everything that posted o the html page
    total_marks=600
    obtained_marks=0
    percentage=0
    if request.method=='POST':
        physics=float(request.form['physics'])
        chemistry=float(request.form['chemistry'])
        maths=float(request.form['maths'])
        biology=float(request.form['biology'])
        english=float(request.form['english'])
        urdu=float(request.form['urdu'])

        obtained_marks=physics+chemistry+maths+biology+english+urdu
        percentage=(obtained_marks*100)/600
        
        return redirect(url_for('result',per=percentage))
        


if __name__=='__main__':
    app.run(debug=True)