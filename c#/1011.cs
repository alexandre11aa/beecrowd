using System;
using System.Globalization;

class URI {

    static void Main(string[] args) {

        string input = Console.ReadLine();
        int r = int.Parse(input);

        double volume = (4.0/3) * 3.14159 * r * r * r;

        Console.WriteLine($"VOLUME = {volume.ToString("F3", CultureInfo.InvariantCulture)}");

    }      
}