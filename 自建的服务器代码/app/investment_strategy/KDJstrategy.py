import talib


# KDJ指标对应的策略
def KDJstrategy(data,period):
    days=period
    for i in range(data.shape[0] - days - 1):  # data.shape[0]代表data的行数.
        X = data[i:i + days, :]
        all_high=X[:,1]
        # print type(all_high[0])
        # print all_high
        all_low=X[:,2]
        all_close=X[:,3]

        slowk, slowd = talib.STOCH(all_high, all_low, all_close,
                                   fastk_period=9,
                                   slowk_period=3,
                                   slowk_matype=0,
                                   slowd_period=3,
                                   slowd_matype=0
                                   )
        # print "slowk:", slowk
        # print "leng of slowk:", len(slowk)
        slowd_copy = slowd
        slowk_copy = slowk
        # print "slowd:", slowd_copy
        close_real = all_close
        #J线图
        slowj = 3 * slowk_copy - 2 * slowd_copy
        #画图表示
        # normal = []
        # high_normal = []
        # print "j线：", slowj
        # long = len(slowj)
        # while long:
        #     normal.append(int(10))
        #     high_normal.append(int(90))
        #     long -= 1
        # print "常数线;", normal
        # x = np.linspace(0, len(slowk_copy), len(slowk_copy))
        # plt.subplot(2, 1, 1)  # （行，列，活跃区）
        # plt.title("red is slowd And orange is J")
        # plt.plot(x, slowk_copy)
        # plt.plot(x, slowd_copy, 'r')
        # plt.plot(x, slowj)
        # plt.plot(x, normal)
        # plt.plot(x, high_normal, 'k')
        #
        # # plt.plot(x,int(20))
        # # plt.plot(x,80)
        # plt.subplot(2, 1, 2)
        # plt.plot(x, close_real)
        # # plt.scatter(slowd,'g--')
        # plt.show()

        # 获得最近的kd
        slowk = slowk[-1]
        slowd = slowd[-1]
        if slowk > 90 or slowd > 80:
            print "超买区，股价有可能下跌，建议卖出股票"
        if slowk < 10 or slowd < 20:
            print "超卖区，股价有可能上涨，建议买股"

