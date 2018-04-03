import pathlib
import textdistance
from fuzzywuzzy import fuzz

if __name__ == "__main__":
	string_a = 'test'
	string_b = 'text'
	fuzz_result = fuzz.ratio(string_a, string_b)
	result = textdistance.hamming(string_a, string_b)
	print("Fuzzy Result: ", fuzz_result)
	for function_name in dir(textdistance):
		try:
			function = getattr(textdistance, function_name)

			result = function(string_a, string_b)
			if isinstance(result, (int,float)):
				print("{}\t{}".format(function_name, result))
		except:
			pass