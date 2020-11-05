from numpy import prod

def factors(n):
	factors_dict = dict()
	while n > 1:
		for i in range(2, n+1):
			if n % i == 0:
				n = n // i
				if str(i) not in factors_dict:
					factors_dict[str(i)] = 0
				factors_dict[str(i)] += 1
				break
	return factors_dict

def convertFracts(lst):
	total = dict()

	for item in lst:
		denominator = item[1]
		for f, v in factors(denominator).items():
			if f not in total or v > total[f]:
				total[f] = v
	denominator = prod([int(k) ** v for k, v in total.items()])
	
	for item in lst:
		item[0] = item[0] * (denominator // item[1])
		item[1] = denominator
	return lst
