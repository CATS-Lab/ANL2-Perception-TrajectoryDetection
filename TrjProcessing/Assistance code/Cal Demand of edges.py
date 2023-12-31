import pandas as pd
import datetime

import matplotlib.pyplot as plt
import cv2

df = pd.read_csv("/media/ubuntu/ANL/Data1_lane_xy_va.csv")
Veh_info = pd.read_csv("/media/ubuntu/ANL/Veh_info.csv")

start_t = '20221111160315.1'
start_t_sec = 0.1 + (datetime.datetime.strptime('20221111160315', "%Y%m%d%H%M%S") - datetime.datetime(2022, 11, 11,
                                                                                                      16)).total_seconds()

start_end_list = {}
for i, row in Veh_info.iterrows():
    start_end = tuple([Veh_info.at[i, 'edge_start'], Veh_info.at[i, 'edge_end']])
    if start_end not in start_end_list.keys():
        start_end_list[start_end] = [Veh_info.at[i, 'id']]
    else:
        start_end_list[start_end].append(Veh_info.at[i, 'id'])

for start_end in list(start_end_list.keys()):
    im = plt.imread("/media/ubuntu/ANL/Data/3Merging/20221111160315.1.merge.jpg")
    implot = plt.imshow(im)
    for veh in start_end_list[start_end]:
        d = df[df['id'] == veh]
        plt.scatter(d['x_pix'].tolist(), d['y_pix'].tolist(), s=2, color="blue")
    plt.gca().set_aspect(1)
    plt.legend()
    plt.savefig("/home/ubuntu/Documents/TrjProcessing/demand_pic/" + str(start_end) + '.jpg')
    # plt.show()
    plt.clf()

# for i in range(2): # 算2个5min
#     t1 = start_t_sec + 5*60*i
#     t2 = start_t_sec + 5*60*(i+1)
#     L = df[(df['t_sec'] >= t1) & (df['t_sec'] < t2)].index
#     pass
