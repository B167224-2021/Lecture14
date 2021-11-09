#!/usr/local/bin/python3
def count_letter(seq, letter):
	count = seq.upper().count(letter.upper())
	percent = (count/len(seq))*100
	return (percent)

#seq ="MSRSLLLRFLLFLLLLPPLP"
#letter ="M"
#print(count_letter(seq, letter))
assert round(count_letter("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)
assert round(count_letter("MSRSLLLRFLLFLLLLPPLP", "r")) == round(10)
assert round(count_letter("MSRSLLLRFLLFLLLLPPLP", "L")) == round(50)
assert round(count_letter("MSRSLLLRFLLFLLLLPPLP", "Y")) == round(0)
