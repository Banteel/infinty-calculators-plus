#!/usr/bin/env python3
# InfintyPlus
# based on Copyright (c)

#	Copyright (c) 2025 (InfintyNow), Copyright (c) 2027 (InfintyPlus) Trevor McQuaker
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted under the terms of the Apache-2.0

#	Copyright 2025, 2027 Trevor McQuaker

#Licensed under the Apache License, Version 2.0 (the "Apache-2.0");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at

#http://www.apache.org/licenses/LICENSE-2.0

#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.



# 	A Sub-calculator (named):
#	"InfintyPlus""
#	The sub-calculator located here in the Python file is the results of sub-calculations permutated from two seporate equations performing the exact same results, for example here is always consistently the number "one".



# 	A Sub-calculator (named):
#	"InfintyPlus""
#	The sub-calculator located here in the Python file is the results of sub-calculations permutated from two seporate equations performing the exact same results, for example here is always consistently the number "one".

import os
#import numpy as np
import math
from math import ceil
from decimal import Decimal, localcontext, InvalidOperation

def InfinityPlus():
	print('		Number Sub-Calculator: "InfinityPlus"')
	
	with localcontext() as ctx:
		ctx.prec = 100000000
		while True:
			try:
				print('   "Input Whole Numbers (21), Fractions (.21), Whole number with fraction (21.21), or Whole number with fraction including "exponent" eg. "21.21e21" or "21.21e-21"')
				num1 = input('   \n   Type "quit" or Enter value #1:\n').strip().lower()
				if num1 == "quit":
					break
					
				num2 = input('   \n   Type "quit" or Enter value #2:\n').strip().lower()
				if num2 == "quit":
					break
				
				a = Decimal(num1)
				b = Decimal(num2)
				
			except (ValueError, InvalidOperation):
				print('   Error: Please enter valid numbers in scientific or decimal format. (ex. 21, 21.21, .21, 21.21e21 or enter  "quit" to close.')
				continue
				
			p1 = Decimal(a / b)
			p2 = Decimal(a - b)
			eq1 = p1 - (p2 / b)
			print(f'\n   Calibrator Macro: a ÷ b - (a - b) ÷ b =   {eq1: .2g}')
			result1 = a / b
			print(f'   A: a ÷ b\n   ={result1.normalize(): .120g}')
			result2 = (a / b) - (a - b)
			print(f"   B: a ÷ b - (a - b)\n   ={result2: .120g}")
			result3 = b - (a - b) / b
			print(f"   C: b - (a - b) ÷ b\n   ={result3: .120g}")
			result4 = b - (a - b)
			print(f"   D: b - (a - b)\n   ={result4: .120g}")
			result5 = a - b
			print(f"   E: (a - b)\n   ={result5: .120g}")
			result6 = (a - b) / b
			print(f"   F: (a - b) ÷ b\n   ={result6: .120g}")
				
			eq2 = (((a / b) / a) * b)
			print(f"\n   Calibrator Micro: a ÷ b ÷ a × b = {eq2: .2g}")
			result7 = a / b
			print(f"   H:  a ÷ b\n   ={result7: .120g}")
			result8 = (a / b) / a
			print(f"   I: a ÷ b ÷ a\n   ={result8: .120g}")
			result9 = (b / a) * b
			print(f"   J:  b ÷ a × b\n   ={result9: .120g}")
			result10 = b / a
			print(f"   K: b ÷ a\n   ={result10: .120g}")
			result11 = a * b
			print(f"   L: a × b\n   ={result11: .120g}")
			input("\n   Program paused.\n   Press the key (Enter or Return) to Reset Program and input new numbers.\n\n")
			
		if os.name == 'nt':
			os.system('cls')
		else:
			os.system('clear')
	print('\n   "InfintyPlus" script closed.\n')
			
if __name__ == "__main__":
	InfinityPlus()

#def format_repeating(n, d):
#    res = [str(n // d), "."]
#    rem_map = {}
#    rem = n % d
#    while rem != 0 and rem not in rem_map:
#        rem_map[rem] = len(res)
#        rem *= 10
#        res.append(str(rem // d))
#        rem %= d
#    if rem != 0: # If it repeats
#        res.insert(rem_map[rem], "(")
#        res.append(")")
#    return "".join(res).rstrip(".")

#from fractions import Fraction

#def format_exact(a, b):
#    f = Fraction(a, b)
#    if f.denominator == 1:
#        return str(f.numerator)
#    return f"{f.numerator}/{f.denominator}"
