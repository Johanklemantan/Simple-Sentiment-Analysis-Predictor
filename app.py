from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__, template_folder='template')
    
filename = 'sentiment_analysis'
model = joblib.load(filename)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method=='POST':
        input = request.form

        df_to_predict = pd.Series(
            input['text']
        )

        prediksi = model.predict(df_to_predict)

        if prediksi == 0:
            res = 'Negative'
        else:
            res = 'Positive'

        return render_template('result.html', data=input, pred=res)

if __name__ == '__main__':


    app.run(debug=True)