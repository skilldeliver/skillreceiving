# Complete the repeatedString function below.
# https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
def repeatedString(s, n):
    return s.count("a") * int(n / len(s)) + s[:n%len(s)].count("a")

