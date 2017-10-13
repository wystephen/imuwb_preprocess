# -*- coding:utf-8 -*-
# Created by steve @ 17-10-13 上午8:34
'''
                   _ooOoo_ 
                  o8888888o 
                  88" . "88 
                  (| -_- |) 
                  O\  =  /O 
               ____/`---'\____ 
             .'  \\|     |//  `. 
            /  \\|||  :  |||//  \ 
           /  _||||| -:- |||||-  \ 
           |   | \\\  -  /// |   | 
           | \_|  ''\---/''  |   | 
           \  .-\__  `-`  ___/-. / 
         ___`. .'  /--.--\  `. . __ 
      ."" '<  `.___\_<|>_/___.'  >'"". 
     | | :  `- \`.;`\ _ /`;.`/ - ` : | | 
     \  \ `-.   \_ __\ /__ _/   .-` /  / 
======`-.____`-.___\_____/___.-`____.-'====== 
                   `=---=' 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
         佛祖保佑       永无BUG 
'''


import numpy as  np

import scipy as sp

import matplotlib.pyplot as plt

import os


import UwbDataPreprocess

if __name__ == '__main__':

    dir_name = "/home/steve/Data/IU/80/"
    uwb_data = np.zeros(1)
    imu_data = np.zeros(1)

    for name in os.listdir(dir_name):
        if 'uwb' in name:
            # uwb_data = np.loadtxt(dir_name+name,delimiter=',')
            udp = UwbDataPreprocess.UwbDataPre(dir_name)
            udp.save()
            uwb_data = np.loadtxt(dir_name+'uwb_result.csv',delimiter=',')


        if 'imu' in name:
            imu_data = np.loadtxt(dir_name+name,delimiter=',')


    plt.figure()
    plt.plot(imu_data[:,0],'r')
    plt.plot(uwb_data[:,1],'b')
    plt.show()



