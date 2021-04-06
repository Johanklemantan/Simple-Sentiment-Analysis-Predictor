# Simple-Sentiment-Analysis-Predictor

Create a simple sentiment analysis predictor from 40000 corpus of IMDB movie comments..
This model has 80% accuracy to predict validation model (5000 datas)

How to run this code :
1. Open the ipynb file
2. Run, and joblib file will be generated
3. Go run the app.py and open local network 5000

Preparation to create this model :
1. make lowercase
2. change main contraction (y'all to you all)
3. remove numbers (appearantly number is not so important)
4. remove punctuation
5. remove white space
6. remove stopwords

Pipelines :
1. Tfidf vectorizer
2. N grams = 2
3. Model = Logistic Regression :( and Multinomial Gaussian Bayes

Result : 
Logistic Regression
<img src = '../logreg.PNG'>

Multinomial Gaussian Bayes
<img src = '../MNB.PNG'>

This model is still not recognize a lot of common words that is not available in a corpus.

Further approach like deep learning (transfer learning) is applicable for this case.

## Thankyou. Happy Coding !
