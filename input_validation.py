# Input validation script I had to wrote for a recruitment (not so fancy but still working :p)

# Requirements:
# 1. Strip andy <script> expression
# 2. Shorten the input to max 50 chars.
# 3. Remove any quotation marks
# 4. URL-decode the input
# 5. If any of the above were deleted, go back to step 1


import re
import urllib.parse


def validate():

	input_original = input('Validate your input: ')
	i = 0	# ERROR DETECTION


	# SCRIPT TAG DETECTION

	if re.match(".*<.*?(s|S)\s*(c|C)\s*(r|R)\s*(i|I)\s*(p|P)\s*(t|T).*\/?>.*", input_original):
		print("Script tag detected! Deleting script tags...\n")

		input_original = re.sub('<.*?(s|S)\s*(c|C)\s*(r|R)\s*(i|I)\s*(p|P)\s*(t|T).*\/?>', "", input_original)
		print("Replaced input:", input_original)
		i = i + 1





	# INPROPRER LENGTH DETECTION

	elif not re.match("^.{1,50}$", input_original):
		print("No input or input too long!")
		i = i + 1




	# QUOTATION MARKS DETECTION

	elif (re.match(".*[\'].*", input_original) or re.match(".*[\"].*", input_original)):
		print("Quotation Error! Deleting quotations...\n")

		input_original = re.sub("\'|\"", "", input_original)
		print("Replaced input:", input_original)
		i = i + 1



	# URL-decoding

	input_decoded = urllib.parse.unquote_plus(input_original)

	if not input_decoded == input_original:
		print("URL-decoded input:", input_decoded)
		print("URL-decoding raised an alert!")
		i = i + 1

	if i == 0:
		print("input OK")
	else:
		print("Let's try again...\n")
		validate()

	input("Press enter to continue...")





validate()





# Tested for:

# aa"bb
# aa'bb
# 'aabb
# aabb'
# "aabb
# aabb"
# '"aabb
# "'aabb
# aabb"'
# aabb'"
# aa"bb"cc
# aa'bb'cc
# aa"'bb'"cc
# "'"''"

# <script>
# aa<script>bb
# <ScRiPt>
# aa<ScRiPt>bb
# <sC rI pt>
# aa<sC rI pt>bb
# <s c r i p t>
# aa<s c r i p t>bb
# <SCRIPT>
# <   Scrip     t>
# </script>
# </scri pt>
# </SCript>
# <script>alert(1)</script>
# "><script>alert("foo")</script>
# %3Cscript%3Ealert(1)%3C/script%3E

