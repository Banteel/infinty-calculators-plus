#!/usr/bin/env python3
# InfintyPlus
# based on Copyright (c)

#        Copyright (c) 2025 (InfintyNow), Copyright (c) 2027 (InfintyPlus) Trevor McQuaker
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted under the terms of the Apache-2.0

#        Copyright 2025, 2027 Trevor McQuaker

#Licensed under the Apache License, Version 2.0 (the "Apache-2.0");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at

#http://www.apache.org/licenses/LICENSE-2.0

#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.


#         A Sub-calculator (named):
#        "InfintyPlus""
#        The sub-calculator located here in the Python file is the results of sub-calculations permutated from two seporate equations performing the exact same results, for example here is always consistently the number "one".

import os
#import numpy as np
import math
import sys
from decimal import Decimal, localcontext, Context, InvalidOperation

def InfinityPlus():
	num1 = None
	num2 = None
	num3 = None
	focus = None
	yesorno = None
	
	print('          Number Sub-Calculator: "InfinityPlus"')
	
	with localcontext() as ctx:
		ctx.prec = 100000000
		
		while True:
			if num1 == 'q' or num2 == 'q' or num3 == 'q' or focus == 'q' or yesorno == 'q':
				break
			yesorno = None
			try:
				print('    Input Whole Numbers (21), Fractions (.21), Whole number with fraction (21.21), or Whole number with fraction including "exponent" eg. "21.21e21" or "21.21e-21')
				
				num1 = input('   \n   Input "q" to Quit or input value for #1:\n').lower()
				a = Decimal(num1)
			except (ValueError, InvalidOperation):
				if num1 == 'q':
					quit()
				else:
					print('   Error: Please input a valid number in scientific or decimal format. (ex. 21, 21.21, .21, 21.21e21 or input "q" to quit.')
					continue
			finally:
				pass

			try:
				num2 = input('   \n   Input "q" to Quit or input value for #2:\n').lower()
				b = Decimal(num2)
			except (ValueError, InvalidOperation):
				if num2 == 'q':
					quit()
				else:
					print('   Error: Please input a valid number in scientific or decimal format. (ex. 21, 21.21, .21, 21.21e21 or input "q" to quit.')
					continue
			finally:
				pass

			try:
				num3 = input('   \n   Input "q" to Quit or input decimal length value:\n').lower()
				c = Decimal(num3)
				tempc = c
			except (ValueError, InvalidOperation):
				if num3 == 'q':
					quit()
				else:
					print('   Error: Please input a valid number in scientific or decimal format. (ex. 21, 21.21, .21, 21.21e21 or input "q" to quit.')
					continue
			finally:
				pass

			while True:
				if num1 == 'q' or num2 == 'q' or num3 == 'q' or focus == 'q' or yesorno == 'q' or yesorno == 'n':
					break
				try:
					if focus == None or yesorno == 'n' or (focus in 'abcdef' and yesorno == 'y'):
						eq1 = (a / b) - ((a - b) / b)
						print(f'\n   Macro Calibrator:\n   a ÷ b - (a - b) ÷ b\n   =   {eq1: .2g}')
					elif focus in 'abcdefghijkl':
						print(f'\n   You selected: {focus.upper()}')
					else:
						print('   Invalid input. Please input a letter from (a-k) or input "q" to Quit.')
						continue
	
					if focus == 'a' or focus == None:
						result1 = a / b
						print(f'\n   A: a ÷ b\n   =   {result1: .{c}g}')
	
					if focus == 'b' or focus == None:
						result2 = (a / b) - (a - b)
						print(f"\n   B: a ÷ b - (a - b)\n   =   {result2: .{c}g}")
	
					if focus == 'c' or focus == None:
						result3 = b - (a - b) / b
						print(f"\n   C: b - (a - b) ÷ b\n   =   {result3: .{c}g}")
	
					if focus == 'd' or focus == None:
						result4 = b - (a - b)
						print(f"\n   D: b - (a - b)\n   =   {result4: .{c}g}")
	
					if focus == 'e' or focus == None:
						result5 = a - b
						print(f"\n   E: (a - b)\n   =   {result5: .{c}g}")
	
					if focus == 'f' or focus == None:
						result6 = (a - b) / b
						print(f"\n   F: (a - b) ÷ b\n   =   {result6: .{c}g}")
	
					if focus == None or yesorno == 'n' or (focus in 'ghijk' and yesorno == 'y'):
						eq2 = (((a / b) / a) * b)
						print(f"\n   Micro Calibrator:\n   a ÷ b ÷ a × b\n   =   {eq2: .2g}")
	
					if focus == 'g' or focus == None:
						result7 = a / b
						print(f"\n   G:  a ÷ b\n   =   {result7: .{c}g}")
	
					if focus == 'h' or focus == None:
						result8 = (a / b) / a
						print(f"\n   H: a ÷ b ÷ a\n   =   {result8: .{c}g}")
	
					if focus == 'i' or focus == None:
						result9 = (b / a) * b
						print(f"\n   I:  b ÷ a × b\n   =   {result9: .{c}g}")
	
					if focus == 'j' or focus == None:
						result10 = b / a
						print(f"\n   J: b ÷ a\n   =   {result10: .{c}g}")
	
					if focus == 'k' or focus == None:
						result11 = a * b
						print(f"\n   K: a × b\n   =   {result11: .{c}g}")
				finally:
					pass
#				except (ValueError, InvalidOperation):
#					print('\n   Invalid input. Please input a letter from (a-k) or input "q" to Quit.')
	
				while True:
					if num1 == 'q' or num2 == 'q' or num3 == 'q' or focus == 'q' or yesorno == 'q' or yesorno == 'n':
						break
					try:
						yesorno = input('\n   Program paused.\n   Change the decimal amount for an output from (a to k)?\n   (y) = Choose a permutation and a decimal amount. \n   (n) = Choose new Work Numbers for Sub-calculations.\n   (d) = Display previous Sub-calculations again  \n   (q) = Quit.\n').lower()
		
						if yesorno == 'q':
							break
						elif yesorno == 'y':
							focus = input('\n   Choose a Permutation letter output from (a to k):\n').lower()
							num3 = input('\n   Program paused.\n   Input a number to change it\'s amount of decimals:\n').lower()
							c = num3
							break
						elif yesorno == 'd':
							focus = None
							c = tempc
							break
						elif yesorno == 'n':
							focus = None
							num1 = None
							num2 = None
							num3 = None
							break
						else:
								print('\n   Invalid input. Choose input "y" or "n" or "d" or "q".')
					except (ValueError, InvalidOperation):
						if yesorno == 'q':
							break
						else:
							continue
					finally:
						pass

#		if os.name == 'nt':
#			os.system('cls')
#		else:
#			os.system('clear')
					
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