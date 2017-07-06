#coding=utf-8


from sklearn import preprocessing
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV


def getpre_GBDT(data, period):
    # 最优参数
    parameters = {'n_estimators': [500], 'max_features': ('auto', 'log2'), \
                  'max_depth': [6], 'min_samples_leaf': [1]}

    data = preprocessing.scale(data)

    print "标注化处理后的结果：", data[0, :]
    i = 0
    t = 0.0  # t : 预测成功次数。
    m = 0.0  # m : 预测上涨，且真实情况上涨的次数。
    e = 0.0  # e : 预测上涨，但真实情况下跌的次数。
    days = period

    predictvalue = 0  # open  close   high    low
    for i in range(data.shape[0] - days - 1):  # data.shape[0]代表data的行数.
        X = data[i:i + days, :]
        y = data[i + 1:i + days + 1, predictvalue]
        # 网格搜索寻找最优参数
        clf = GridSearchCV(GradientBoostingRegressor(), parameters)

        clf.fit(X, y)

        X2 = data[i:i + days + 1, :]
        y_pre = clf.predict(X2)
        y_real = data[i + 1:i + days + 2, predictvalue]
        y_real_change = y_real[-1] - y_real[-2]
        y_pre_change = y_pre[-1] - y_pre[-2]
        if y_real_change * y_pre_change > 0:
            t = t + 1
        if y_pre_change > 0:

            if y_real_change > 0:
                m = m + 1
            else:
                e = e + 1
    right_rate = t / (len(data) - days) * 100
    up_right_rate = m / (m + e) * 100

    print "预测的正确率：", right_rate
    print"预测涨的正确率：", up_right_rate
    return right_rate