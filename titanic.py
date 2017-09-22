# -*- coding:utf-8 -*- 

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import numpy as np
import pandas as pd

PATH = "/home/lianxin/github/ml/src/titanic_survival_exploration-master/titanic_data.csv"
full_data = pd.read_csv(PATH)

outcomes = full_data["Survived"]
data = full_data.drop("PassengerId", axis=1)

def accuracy_score(truth, pred):
    """ 返回 pred 相对于 truth 的准确率 """
    
    # 确保预测的数量与结果的数量一致
    if len(truth) == len(pred): 
        
        # 计算预测准确率（百分比）
        return "Predictions have an accuracy of {:.2f}%.".format((truth == pred).mean()*100)
    
    else:
        return "Number of predictions does not match number of outcomes!"

def prediction_0(data):
    """ 不考虑任何特征，预测所有人都无法生还 """

    predictions = []
    for _, passenger in data.iterrows():
        
        # 预测 'passenger' 的生还率
        predictions.append(0)
    
    # 返回预测结果
    return pd.Series(predictions)

predictions = prediction_0(data)
print accuracy_score(outcomes, predictions)

def prediction_1(data):
    """ 只考虑一个特征，如果是女性则生还 """
    predictions = []
    for _, passenger in data.iterrows():
        if passenger["Sex"] == "female":
            predictions.append(1)
        else:
            predictions.append(0)
    
    # 返回预测结果
    return pd.Series(predictions)

predictions = prediction_1(data)
# print accuracy_score(outcomes, predictions)

def predictions_2(data):
    """ 考虑两个特征: 
            - 如果是女性则生还
            - 如果是男性并且小于10岁则生还 """

    predictions = []
    for _, passenger in data.iterrows():
        
        if passenger["SibSp"] > 4:
            predictions.append(0)
        elif passenger["Sex"] == "female" and passenger["Pclass"] < 3:
            predictions.append(1)
        elif passenger["Sex"] == "female" and passenger["SibSp"] < 2:
            predictions.append(1)
        elif passenger["Pclass"] == 1 and passenger["Age"] < 18:
            predictions.append(1)
        elif passenger["Age"] < 10:
            predictions.append(1)
        elif passenger["Fare"] > 270:
            predictions.append(1)
        else:
            predictions.append(0)
    
    # 返回预测结果
    return pd.Series(predictions)

predictions = predictions_2(data)
print accuracy_score(outcomes, predictions)
