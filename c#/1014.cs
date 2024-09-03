using System;
using System.Globalization;

class URI {

    static void Main(string[] args) {

        string input_a = Console.ReadLine();
        string input_b = Console.ReadLine();
        
        int a = int.Parse(input_a);
        double b = double.Parse(input_b, CultureInfo.InvariantCulture);

        double consume = a / b;

        Console.WriteLine($"{consume.ToString("F3", CultureInfo.InvariantCulture)} km/l");
    }      
}
