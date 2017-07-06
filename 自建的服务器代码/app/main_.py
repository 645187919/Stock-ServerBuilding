#coding=utf-8
import json

import talib
from flask import Flask, jsonify

from app import deal_datas
from app.ml_algorithm import svm
from app.ml_algorithm import randomForest
from app.ml_algorithm import GBDT
from models import to_json

app = Flask(__name__)

# 路由函数
@app.route('/')
def index():
    return '<p><h4>sucessful</h4></p>'
@app.route('/ml')
def user():
    def tojson( ):

        json_post={
            "resultcode": "200",
            "reason": "search sucessfully",
            "result":{
                'right_rate':right_rate,
                'pre_change':pre_change

            }

            }


        print "json:",json_post
        return json.dumps([json_post])

    data = deal_datas.get_data(r'G:\example\dates\sh600000.csv')
    data = data[::-1]
    print "data的类型：", type(data)
    print "倒序后的数据：", data
    # k日均线k的值
    k = 1
    origal_data, copy_data = deal_datas.deal_data(data, k)

    right_rate,pre_change= svm.getpre_SVM(origal_data, copy_data,150)
    # right_rate=randomForest.getpre_RFR(sma_deal_data, 280)
    # right_rate=GBDT.getpre_RFR(sma_deal_data, 280)

    return tojson()


# with app.test_request_context():
#     print url_for('index')
#     print url_for('user',name='tom')
if __name__ == '__main__':
    app.run(debug=True)

