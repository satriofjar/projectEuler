package main

import "fmt"

func sol1(lim int) int {
	var result int
	for i := 0; i < lim; i++ {
		if i%3 == 0 || i%5 == 0 {
			result += i
		}
	}
	return result
}

func main() {

	fmt.Println(sol1(1000))
}
