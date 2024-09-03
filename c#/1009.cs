using System;
using System.Globalization;

class URI {

    static void Main(string[] args) { 

        Console.Write("");
        string input_a = Console.ReadLine();

        Console.Write("");
        string input_b = Console.ReadLine();
        double b = double.Parse(input_b, CultureInfo.InvariantCulture);

        Console.Write("");
        string input_c = Console.ReadLine();
        double c = double.Parse(input_c, CultureInfo.InvariantCulture);

        double salary = b + c * 0.15;

        Console.WriteLine($"TOTAL = R$ {salary.ToString("F2", CultureInfo.InvariantCulture)}");

    }

}