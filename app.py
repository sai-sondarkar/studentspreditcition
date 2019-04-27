import numpy as np
#need to 'conda install flask' for this to work
from flask import Flask, abort, jsonify, request
import pickle


my_random_forest = pickle.load(open("students_data_ml.pkl", "rb"))

app = Flask(__name__)

@app.route('/', methods=['POST'])
def make_predict():
    #all kinds of error checking should go here
    data = request.get_json(force=True)
    ssc = data["ssc"]
    hsc = data["hsc"]
    set =0

    if  ssc> 70 and hsc>70:
        set = 1
    elif ssc> 60 and hsc>60:
        set = 2
    else:
        set = 3


    #convert our json to a numpy array
    # predict_request = [data['nu'],data['ps1'],data['ps2'],data['ps3'],data['pm1'],data['pm2'],data['pm3'],data['sal'],data['p']] 
    # predict_request = np.array(predict_request).reshape(1,-1)
    #np array goes into random forest, prediction comes out
    # y_hat = my_random_forest.predict(predict_request)
    #return our prediction
    y_hat = set
    output = {'job_set': y_hat}
    print(output)
    return jsonify(output)

if __name__ == '__main__':
    app.run()



