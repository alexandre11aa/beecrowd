using System;
using System.Globalization;

class URI {

    static void Main(string[] args) {

        string input_a = Console.ReadLine();

        double a = double.Parse(input_a);
                
        if ((a >= 0) && (a <= 25)) {
            Console.WriteLine("Intervalo [0,25]");
        } else if ((a > 25) && (a <= 50)) {
            Console.WriteLine("Intervalo (25,50]");
        } else if ((a > 50) && (a <= 75)) {
            Console.WriteLine("Intervalo (50,75]");
        } else if ((a > 75) && (a <= 100)) {
            Console.WriteLine("Intervalo (75,100]");
        } else {
            Console.WriteLine("Fora de intervalo");
        }
    }    
}
