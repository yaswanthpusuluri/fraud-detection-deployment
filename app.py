import pickle
from flask import Flask,render_template,request


model=pickle.load(open('model.pkl','rb'))

app=Flask(__name__) #create the flask object

@app.route('/')  #some open opens the sever
def htmlPage():
    return render_template('index.html')

@app.route('/predict',methods=['post'])
def predict():
    #collecting data from form
    fd=float(request.form['fd'])
    fd1=float(request.form['fd1'])
    fd2=float(request.form['fd2'])
    fd3=float(request.form['fd3'])
    fd4=float(request.form['fd4'])
    result=model.predict([[fd,fd1,fd2,fd3,fd4]])
    if result[0] == 0:
        return render_template('index.html',result="fraud is not detected")
    else :
        return render_template('index.html',result1="fraud is detected")
    
    


if __name__=="__main__":
    app.run(host='127.0.0.1',port=5001,debug=True)