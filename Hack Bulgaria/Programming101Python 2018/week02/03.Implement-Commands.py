import sys
import os
from random import randint

def cat(arguments):
    file = open(arguments, "r")
    for i in file.readlines():
        print(i)

def cat2(arguments):
    for i in arguments:
        file = open(i, "r")
        for j in file.readlines():
            print(j, end="")
        file.close()
        if i != arguments[len(arguments) - 1]:
            print("\n")

def generate_numbers(filename, numbers):
    
    string = ""
    for i in range(numbers):
        string += str(randint(0, 1000)) + " "

    file_o = open(filename, "w")
    file_o.write(string)
    file_o.close()

def sum_numbers(filename):

    total = 0
    file = open(filename, "r")
    for i in file.readline().split():
        total += i

    print(total)

def size_of(directory):
    total = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total += os.path.getsize(fp)

    ext = " B"
    if total >= 1000 and total < 1000000:
        ext = " KB"
        total /= 1000
    elif total >= 1000000 and total < 1000000000:
        ext = " MB"
        total /= 1000000
    elif total >= 1000000000 and total < 1000000000000:
        ext = " GB"
        total /= 1000000000
    elif total >= 1000000000000:
        ext = " TB"
        total /= 1000000000000

    total = int(total)
    print(str(total) + ext)

def count_cwl(mode, filename):

    file = open(filename, "r")
    count = 0
    string = ""

    if mode == "chars":
        for line in file.readlines():
            count += len(line)
    elif mode == "words":
        for line in file.readlines():
            for let in line:
                string += let
            count += len(string.split())
            string = ""
    elif mode == "lines":
        count = len(file.readlines())

    file.close()

    print(count)      
        

def main():
    print("1. Implement the cat command - Print file contents")
    print("-----------------------------------------")
    cat(input()) #files/file.txt
    print("-----------------------------------------")
    print("    ")
    print("2. Cat multiple files")
    print("-----------------------------------------")
    cat2(input().split()) #files/file.txt files/file2.txt
    print("-----------------------------------------")
    print("    ")
    print("3. Generate file with random integers")
    print("-----------------------------------------")
    generate_numbers(input(), int(input())) #files/numbers.txt
    print("-----------------------------------------")
    print("    ")
    print("4. Sum integers from file")
    print("-----------------------------------------")
    sum_numbers(input()) #files/numbers.txt
    print("    ")
    print("5. Implement an alternative to du -h command")
    print("-----------------------------------------")
    size_of(input()) #files/directory
    print("-----------------------------------------")
    print("    ")
    print("6. Count characters, words or lines")
    print("-----------------------------------------")
    print("-----------------------------------------")
    inp = input().split()                            # chars, words or lines and files/filename
    count_cwl(inp[0], inp[1])
    print("-----------------------------------------")

if __name__ == '__main__':
    main()