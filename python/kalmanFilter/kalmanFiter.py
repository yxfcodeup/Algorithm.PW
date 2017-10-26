# -*- coding: utf-8 -*-

"""
 Name:
    kalmanFilter
 Version:
 Author:
    Ployo Wiself
 Language: 
    Python 3.6.0
 Start time:
    2017-10-23 15:00
 Description:
 Input:
 Output:
"""

import os
import sys


"""
# optimal_val: 上一状态最优值
# predict_cov: 预测值的协方差
# control_var: 控制变量
# measure: 测量值
"""
def kalmanFilter(optimal_val , predict_cov , control_var , measure) :
