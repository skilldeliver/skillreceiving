def is_prime(n):
	if n == 2 or n == 3:
		return True
	if n % 2 == 0 or n % 3 == 0:
		return False

	i = 5
	while i * i <= n:
		if n % i == 0 or n % (i+2) == 0:
			return False
		i += 6
	return True

def gap(g, m, n):
	last = 0
	for i in range(m, n + 1):
		if is_prime(i) and last and i - last == g:
			return [last, i]
		elif is_prime(i):
			last = i