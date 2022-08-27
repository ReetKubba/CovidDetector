from flask import Flask,render_template,request
import pickle

#open a file where you stored pickled data
file=open('model.pkl','rb')
clf=pickle.load(file)
file.close()

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def hello_world():
    if request.method=="POST":
        myDict=request.form
        fever=int(myDict['fever'])
        age=int(myDict['age'])
        pain=int(myDict['pain'])
        runnyNose=int(myDict['runnyNose'])
        diffBreath=int(myDict['diffBreath'])
    #input data
        inputFeatures=[fever,pain,age,runnyNose,diffBreath]
        print(inputFeatures)
        infectionProb=clf.predict_proba([inputFeatures])[0][1]
        print(infectionProb)
        return render_template('show.html',inf=round(infectionProb*100))
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)