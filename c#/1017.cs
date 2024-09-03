using System;
using System.Globalization;

class URI {

    static void Main(string[] args) {

        string input_a = Console.ReadLine();
        string input_b = Console.ReadLine();
        
        int a = int.Parse(input_a);
        int b = int.Parse(input_b);

        double consume = a * b / 12.0;

        Console.WriteLine($"{consume.ToString("F3", CultureInfo.InvariantCulture)}");
    }      
}
