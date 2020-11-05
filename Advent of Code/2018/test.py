# num_а = int(input())
# num_b = int(input())
# passes_max = int(input())

# time_to_break = False

# passes_counter = 0

# for A in range(35, 56):
#     if time_to_break:
#         break
#     for B in range(64, 97):
#         if time_to_break:
#             break
#         for x in range(1, num_а + 1):
#             if time_to_break:
#                 break
#             for y in range(1, num_b + 1):
            
#                 if passes_counter > (num_а + num_b) or passes_max == passes_counter:
#                     time_to_break = True
#                     break
#                 print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end="|")

#                 passes_counter += 1

#                 A += 1
#                 B += 1

#                 if A > 55:
#                     A = 35

#                 if B > 96:
#                     B = 64






# for A in range(35, 56, 2):
#     for B in range(64, 97, 2):
#         for x in range(1, a + 1):
#             for y in range(1, b + 1):
#                 print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end="|")

#                 if x == a or y == a:
#                     quit()

#                 if A > 55:
#                     A = 35
#                 if B > 96:
#                     B = 55

# a = int(input())
# b = int(input())
# n = int(input())

a, b, n, A, B = map(int, (input(), input(), input(), '34', '63'))
cs = [(x, y) for x in range(1, a + 1) for y in range(1, b + 1)]
for c in cs:
    A, B, n = A + 1, B + 1, n - 1
    A = 35 if A > 55 else A; B = 64 if B > 96 else B
    print(f"{chr(A)}{chr(B)}{c[0]}{c[1]}{chr(B)}{chr(A)}", end="|")
    quit() if not n else 0

# for x in range(1, a + 1):
#     for y in range(1, b + 1):
#         A += 1
#         B += 1
#         max_n -= 1

#         if A > 55:
#             A = 35
#         if B > 96:
#             B = 64

        

#         if not max_n:
#             quit()

# a = int(input())
# b = int(input())
# max_n = int(input())

#  for x in range()