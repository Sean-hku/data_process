# import matplotlib.pyplot as plt
#
#
# fig, axes = plt.subplots(2, 2, figsize=(12, 12))
# ls1 = [0.6,0.7,0.8,0.9]
# ls2 = [0.6,0.7,0.8,0.9]
# ls3 = [0.6,0.7,0.8,0.9]
# ls4 = [0.6,0.7,0.8,0.9]
# plt.bar(ls1,height=12,ax=axes[0][0])
# plt.show()

#
# import numpy as np
# import matplotlib.pyplot as plt
#
# size = 4
# x = np.arange(size)
# a = [0.6,0.7,0.8,0.9]
# b = [0.6,0.7,0.8,0.9]
# c = [0.6,0.7,0.8,0.9]
#
# total_width, n = 0.8, 3
# width = total_width / n
# x = x - (total_width - width) / 2
# x= [x,x + width,x + 2 * width,x + 3 * width]
# plt.bar(x, a,  width=width, label='a')
# # plt.bar(x + width, b, width=width, label='b')
# # plt.bar(x + 2 * width, c, width=width, label='c')
# plt.legend()
# plt.show()


import matplotlib.pyplot as plt

name_list = ['mAP', 'Precious', 'Recall', 'F1']
num_list = [1.5, 0.6, 1, 0.6]
num_list1 = [1, 2, 0.3, 1]
num_list2 = [0.5, 1, 2, 0.3]
num_list3 = [0.5, 1, 2, 0.3]
x = list(range(len(num_list)))
# x=[0.5,1.5,2.5,3.5]
total_width, n = 0.6, 4
width = total_width / n

plt.bar(x, num_list, width=width, label='COCO', )
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, num_list1, width=width, label='Gray', tick_label=name_list, )
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, num_list2, width=width, label='RGB', tick_label=name_list, )
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, num_list3, width=width, label='RGB', tick_label=name_list, )
plt.legend()
plt.show()