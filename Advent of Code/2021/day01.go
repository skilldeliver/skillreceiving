package main

import (
    "bufio"
    "fmt"
    "os"
    "log"
    "strconv"
)

func main() {
    file, err := os.Open("inputs/day01.txt")

    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    var number, result, counter int

    scanner := bufio.NewScanner(file)

    for scanner.Scan() {
        new_number, _ := strconv.Atoi(scanner.Text())

        if counter != 0 {
            if new_number > number {
                result += 1
            }
        }

        number = new_number
        counter += 1
    }

    fmt.Println("result:", result)

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }

}
