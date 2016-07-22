#!/usr/bin/env python
# -*- coding: utf-8 -*-

__import__("sys").path.append('../')
from random import uniform,randint
from Kernel import Utils
from Kernel import Config
from Kernel import ExtractKeywords

## Cota inferior positiva y menor que n, cota superior positiva mayor que n ##
def hide_number(n,deep,deep_max=3,lower_bound=-10000,upper_bound=10000):
    if deep==deep_max: return str(n)
    else:
	index_op     = randint(0,3)
	if index_op==0: 
	    random_value = uniform(lower_bound,n-1)
	    return "("+hide_number(random_value,deep+1,deep_max,lower_bound,upper_bound)+"+"+hide_number(n-random_value,deep+1,deep_max,lower_bound,upper_bound)+")"
	elif index_op==1:
	    random_value = uniform(n,upper_bound)
	    return "("+hide_number(random_value,deep+1,deep_max,lower_bound,upper_bound)+"-"+hide_number(random_value-n,deep+1,deep_max,lower_bound,upper_bound)+")"
	elif index_op==2:
	    random_value = uniform(lower_bound,n-1)
	    return "("+hide_number(random_value,deep+1,deep_max,lower_bound,upper_bound)+"*"+hide_number(float(n)/random_value,deep+1,deep_max,lower_bound,upper_bound)+")"
	elif index_op==3:
	    random_value = uniform(n,upper_bound)
	    return "("+hide_number(random_value,deep+1,deep_max,lower_bound,upper_bound)+"/"+hide_number(float(random_value)/n,deep+1,deep_max,lower_bound,upper_bound)+")"

def hide_numbers(obj,deep_max_min=3,deep_max_max=5,lower_bound=-10000,upper_bound=10000):
    deep_max = randint(min(deep_max_min,deep_max_max),max(deep_max_min,deep_max_max))
    for i in xrange(len(obj)):
	integers = ExtractKeywords.extract_integer(obj[i])
	for j in xrange(len(integers)): 
	    if int(integers[j])!=0: 
		obj[i] = obj[i].replace(" "+integers[j]+"\n"," "+hide_number(int(integers[j]),0,deep_max,lower_bound,upper_bound)+"\n")
    return obj
