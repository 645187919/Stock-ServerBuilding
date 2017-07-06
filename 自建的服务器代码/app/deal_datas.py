#coding=utf-8
import csv
import numpy as np
import talib



def get_data(filename):
    sample = []
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)  # skipping column names
        for row in csvFileReader:
            sample.append(row)
    print "samples:", sample
    return sample

def deal_data(date,k):
    close=[ ]
    open=[ ]
    high=[ ]
    low=[ ]
    time=[ ]
    volume=[ ]
    for row in date:
        time.append(row[1])
        open.append(float(row[2]))
        high.append(float(row[3]))
        low.append(float(row[4]))
        close.append(float(row[5]))
        volume.append(float(row[7]))

    deal_time = np.reshape(time, (len(time), 1))
    deal_open = np.reshape(open, (len(open), 1))
    # print "sma_open:",type(deal_open[2])
    deal_high = np.reshape(high, (len(high), 1))
    deal_low = np.reshape(low, (len(low), 1))
    deal_close = np.reshape(close, (len(close), 1))
    deal_volume=np.reshape(volume, (len(close), 1))
    # --------------------------------------------------------------------------------
    origal_data = np.hstack((deal_open, deal_high, deal_low,deal_close))
    # origal_data = np.hstack((deal_open, deal_high, deal_low,deal_close,deal_volume))
    copy_data=origal_data
    while k - 1:
        copy_data = np.delete(copy_data, 0, 0)
        k -= 1
    print type(origal_data[0][1])
    print "copy_data:", copy_data
    print "copy_data的长度", len(copy_data)

    print "origal_data:", origal_data
    print "origal_data的长度", len(origal_data)
    print "-----------------------------------"
    return origal_data,copy_data
def MA_deal_data(date,k):

    close = []
    open = []
    high = []
    low = []
    time = []
    for row in date:

        open.append(float(row[0]))
        high.append(float(row[1]))
        low.append(float(row[2]))
        close.append(float(row[3]))


    open_arr = np.array(open)
    high_arr = np.array(high)
    low_arr = np.array(low)
    close_arr = np.array(close)
    time_arr = np.array(time)

    # print "数组的数据是：", close_arr
    days = int(k)  # k天均线

    sma_open = talib.SMA(open_arr, days)
    sma_high = talib.SMA(high_arr, days)
    sma_low = talib.SMA(low_arr, days)
    sma_close = talib.SMA(close_arr, days)
    # print len(sma_close)

    # print "day日均线的数组:", sma_close


    sma_time = np.reshape(time_arr, (len(time_arr), 1))
    sma_open = np.reshape(sma_open, (len(sma_open), 1))
    # print "sma_open:",sma_open
    sma_high = np.reshape(sma_high, (len(sma_high), 1))
    sma_low = np.reshape(sma_low, (len(sma_high), 1))
    sma_close = np.reshape(sma_close, (len(sma_high), 1))
    sma_data = np.hstack((sma_open, sma_high, sma_low, sma_close))
    # print "sma_data",sma_data


    while days - 1:
        sma_data = np.delete(sma_data, 0, 0)
        days -= 1

    sma_deal_data = sma_data
    # print type(sma_deal_data[0][1])
    print len(sma_deal_data)
    print "sma_deal_data:", sma_deal_data


    return sma_deal_data

