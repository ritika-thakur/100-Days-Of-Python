#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
from colorama import Back, Style


def highlight(text):
    output = text
    output = output[:0] + Back.YELLOW + Style.BRIGHT + output[0:] + Style.RESET_ALL 
    print(output,end=" ")
    return

# def highlight_matches(pattern, text, print_output=True):
# 	output = text
# 	len_inc = 0
# 	for match in pattern.finditer(text):
# 		start, end = match.start() + len_inc, match.end() + len_inc
# 		output = output[:start] + Back.YELLOW + Style.BRIGHT + output[start:end] + Style.RESET_ALL + output[end:]
# 		len_inc = len(output) - len(text)  

# 	if print_output:
# 		print(output)
# 	else:
# 		return output

