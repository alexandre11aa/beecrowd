using System;
using System.Globalization;

class URI {

    static void Main(string[] args) { 

        Console.Write("");
        string input_a = Console.ReadLine();
        double a = double.Parse(input_a, CultureInfo.InvariantCulture);

        Console.Write("");
        string input_b = Console.ReadLine();
        double b = double.Parse(input_b, CultureInfo.InvariantCulture);

        Console.Write("");
        string input_c = Console.ReadLine();
        double c = double.Parse(input_c, CultureInfo.InvariantCulture);

        double media = (a * 2 + b * 3 + c * 5) / 10;

        Console.WriteLine($"MEDIA = {media.ToString("F1", CultureInfo.InvariantCulture)}");

    }

}