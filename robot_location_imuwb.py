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

    dir_name = "/home/steve/Data/IU/82/"
    uwb_data = np.zeros(1)
    imu_data = np.zeros(1)

    for name in os.listdir(dir_name):
        if 'pre' in name:
            continue
        if 'uwb' in name:
            # uwb_data = np.loadtxt(dir_name+name,delimiter=',')
            udp = UwbDataPreprocess.UwbDataPre(dir_name)
            udp.save()
            uwb_data = np.loadtxt(dir_name + 'uwb_result.csv', delimiter=',')

        if 'imu' in name:
            imu_data = np.loadtxt(dir_name + name, delimiter=',')

    k = (imu_data[-1, 0] - imu_data[0, 0]) / float(imu_data.shape[0])

    for i in range(1, imu_data.shape[0]):
        imu_data[i, 0] = imu_data[0, 0] + k * i

    print("end time diff:", imu_data[-1, 0] - uwb_data[-1, 0])
    print("start time diff: ", imu_data[0, 0] - uwb_data[0, 0])

    plt.figure()
    plt.plot(imu_data[:, 0], 'r')
    plt.plot(uwb_data[:, 0], 'b')

    plt.figure()

    for i in range(1, imu_data.shape[1] - 1):
        plt.plot(imu_data[:, i], '-+', label=str(i))
    plt.legend()

    plt.figure()
    plt.plot(uwb_data[:, 0], 'b-*')

    # uwb data remodify

    from array import array

    uwb_array = array('d')

    uwb_one_line = np.zeros(uwb_data.shape[1]-1)
    uwb_one_line_time = np.zeros(uwb_data.shape[1]-1)
    interval_time = 0.5

    last_time = uwb_data[0, 0]
    print('uwb data shape:',uwb_data.shape)
    for i in range(uwb_data.shape[0]):
        for j in range(len(uwb_one_line)):
            if (uwb_data[i, j+1] > 0.0):
                uwb_one_line[j] = uwb_data[i, j+1]
        if uwb_data[i, 0] > last_time + interval_time:
            uwb_array.append(last_time)
            for j in range(len(uwb_one_line)):
                uwb_array.append(uwb_one_line[j])
            if i < uwb_data.shape[0]-1:
                last_time = uwb_data[i+1,0]



    uwb_data = np.frombuffer(uwb_array, dtype=np.float)
    uwb_data = uwb_data.reshape([-1,5])

    print(uwb_data.shape)
    plt.figure()
    for i in range(1, uwb_data.shape[1]):
        plt.plot(uwb_data[:, 0], uwb_data[:, i], '-*', label=str(i))
    # plt.plot(uwb_data)
    for i in range(7,10):
        plt.plot(imu_data[:,0],imu_data[:,i]/10.0,'-*',label='imu mag:'+str(i))

    plt.grid()
    plt.legend()


    # plt.figure()
    # plt.title('immatrix')
    # plt.imshow(uwb_data[:,1:])

    np.savetxt(dir_name + 'pre_imu.csv', imu_data)
    np.savetxt(dir_name + 'pre_uwb.csv', uwb_data)
    plt.show()
