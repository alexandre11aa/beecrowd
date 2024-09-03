<<<<<<< HEAD
using System;
using System.Globalization;

class URI {

    static void Main(string[] args) {

        string input = Console.ReadLine();
        int r = int.Parse(input);

        double volume = (4.0/3) * 3.14159 * r * r * r;

        Console.WriteLine($"VOLUME = {volume.ToString("F3", CultureInfo.InvariantCulture)}");

    }      
=======
using System;
using System.Globalization;

class URI {

    static void Main(string[] args) {

        string input = Console.ReadLine();
        int r = int.Parse(input);

        double volume = (4.0/3) * 3.14159 * r * r * r;

        Console.WriteLine($"VOLUME = {volume.ToString("F3", CultureInfo.InvariantCulture)}");

    }      
>>>>>>> 1cfb7856b5cd16d06c82bd088e56144c1fd011c8
}