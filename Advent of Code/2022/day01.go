package main

import (
    "bufio"
    "fmt"
    "os"
    "log"
	"sort"
    "strconv"
)

func sum(array []int) int {  
	result := 0  
	for _, v := range array {  
		result += v  
	}  
	return result  
} 

func partOne(scanner *bufio.Scanner) {
	var elfCalories int = 0
	var maxElfCalories int = 0

    for scanner.Scan() {
		if scanner.Text() == "" {
			if elfCalories > maxElfCalories {
				maxElfCalories = elfCalories
			}
			elfCalories = 0
		} else {
			new_number, _ := strconv.Atoi(scanner.Text())
			elfCalories += new_number
		}
		
	}
	fmt.Println("result:", maxElfCalories)
}


func partTwo(scanner *bufio.Scanner) {
	var elfCalories int = 0
	var elfCaloriesSlice []int

	for scanner.Scan() {
		if scanner.Text() == "" {
			elfCaloriesSlice = append(elfCaloriesSlice, elfCalories)
			elfCalories = 0
		} else {
			new_number, _ := strconv.Atoi(scanner.Text())
			elfCalories += new_number
		}	
	}

	sort.Sort(sort.IntSlice(elfCaloriesSlice))
	fmt.Println(sum(elfCaloriesSlice[len(elfCaloriesSlice)-3:len(elfCaloriesSlice)]))
}


func main() {
    file, err := os.Open("inputs/day01.txt")

    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()
    scanner := bufio.NewScanner(file)
	
	// partOne(scanner)
	partTwo(scanner)

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }

}