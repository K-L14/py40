#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
if __name__ == '__main__':
    a = [9,7,5,3,1]
    N = len(a) 
    print (a) 
    for i in range(len(a) // 2):
        a[i],a[N - i - 1] = a[N - i - 1],a[i]
    print (a)
    