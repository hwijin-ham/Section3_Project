from flask import Flask, render_template, request
#from flask_app.routes import user_routes
import pickle
import csv
import pandas as pd

app = Flask(__name__)
#app.register_blueprint(user_routes.bp)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/index/', defaults={ 'num' : 0 })
@app.route('/index/<num>')
def index_number(num):
    return 'Welcome to Index %i' % int(num)

@app.route('/review', methods=['GET'])
def review():
    name = request.args.get('name')
    tags = request.args.get('tags')
    price = request.args.get('price')
    like = request.args.get('like')

    f = open('/Users/hamhwijin/Section3_Project/selenium/review_modify copy.csv','a')
    wr = csv.writer(f)
    wr.writerow([name, tags, price, like])
    
 
    f.close()

    df =  pd.read_csv("/Users/hamhwijin/Section3_Project/selenium/review_modify copy.csv")
    X = df.drop(['score', 'name'], axis=1)
    print(X)
    encoder = None
    with open('/Users/hamhwijin/Section3_Project/model/encoder.pkl','rb') as pickle_encoder:
        encoder = pickle.load(pickle_encoder)

    reviews_ohe = encoder.transform(X)
    print(reviews_ohe)
    model = None
    with open('/Users/hamhwijin/Section3_Project/model/model.pkl','rb') as pickle_model:
        model = pickle.load(pickle_model)
    
    pred = model.predict(reviews_ohe)
    print(pred)
    return render_template('review.html', name=name, pred=round(pred[-1],1))

if __name__=='__main___':
    app.run(debug=True)