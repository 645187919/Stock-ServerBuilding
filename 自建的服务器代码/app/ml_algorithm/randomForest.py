#coding=utf-8

from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV



def getpre_RFR(data,origal_data,period):
    '''parameters = {'n_estimators':[100,200,300],'min_samples_leaf':[1,2],\
                   'max_features':('auto','log2'),'max_depth':[3,6,9]}'''
    # parameters = {'n_estimators': [10, 20], 'max_features': ('auto', 'log2'), \
    #               'max_depth': [10, 20],'min_samples_leaf':[1,2]}
    # parameters = {'n_estimators': [10], 'max_features':['log2'], \
    #               'max_depth': [60], 'min_samples_leaf': [1]}
    data = preprocessing.scale(data)
    or_date=preprocessing.scale(origal_data)

    print "标注化处理后的结果：", data[0, :]

    i = 0
    t = 0.0  # t : 预测成功次数。
    m = 0.0  # m : 预测上涨，且真实情况上涨的次数。
    e = 0.0  # e : 预测上涨，但真实情况下跌的次数。
    days =period-1

    predictvalue = 0  # open  close   high    low
    for i in range(data.shape[0] - days - 1):  # data.shape[0]代表data的行数.
        X = data[i:i + days, :]
        y = data[i + 1:i + days + 1, predictvalue]
        # 网格搜索寻找最优参数

        clf=RandomForestRegressor(max_features=4 ,n_estimators=100,n_jobs=4)
        clf.fit(X, y)

        X2 = data[i+1:i + days + 1, :]
        y_pre = clf.predict(X2)
        y_real = or_date[i + 2:i + days + 2, predictvalue]
        y_real_change = y_real[-1] - y_real[-2]
        y_pre_change = y_pre[-1] - y_pre[-2]
        if y_real_change * y_pre_change > 0:
            t = t + 1
        if y_pre_change > 0:

            if y_real_change > 0:
                m = m + 1
            else:
                e = e + 1
    acuracy=t / (len(data) - days) * 100

    print "预测的正确率：",acuracy

    print"预测涨的正确率：", m / (m + e) * 100
    return acuracy
