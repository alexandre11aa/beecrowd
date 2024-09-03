package main

import (
	"fmt"
	"math"
)

func main() {

	const pi = 3.14159

	var n, raio float64

	fmt.Scan(&n)

	raio = pi * math.Pow(n, 2)

	fmt.Printf("A=%.4f\n", raio)

}
