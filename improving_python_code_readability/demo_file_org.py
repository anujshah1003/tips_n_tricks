



import sys
import yaml
from utils.dotdict import dotdict 

import os
import logging
import torch
import numpy as np


print (os.getcwd())

path=r'D:\youtube\2022\tips_and_tricks'
new_list=[0,1,2,3,4,5,6,7,8,9,10]
new_list_2=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

new_dict={'a':'apple','b':'ball','c':'cat','d':'dog','e':'egg'}



def get_results(param_a,param_b,param_c,param_d,param_e,param_f,param_g,param_h,param_i):
    result_1=param_a+param_b+param_c
    result_2=param_d+param_e+param_f
    result=result_1+result_2+param_g+param_h+param_i
    return result





def add(a,  b):
    "adding the parameters"
    answer = a + b
    return    answer

def add_2(a,
          b):
    return a+b