#!/usr/local/bin/python3
def aa_percent_v2(seq, aa=["A", "I","L", "M", "F", "W", "Y", "V"]):
	count = 0
	percent = 0
	for i in aa:
		count += seq.upper().count(i.upper())
	percent = (count/len(seq))*100
	print(round(percent,0))
	return round(percent,0)
assert round(aa_percent_v2("MSRSLLLRFLLFLLLLPPLP", ["M"])) == 5
assert round(aa_percent_v2("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])) == 70
assert round(aa_percent_v2("MSRSLLLRFLLFLLLLPPLP")) == 65

