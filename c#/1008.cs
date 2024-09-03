<<<<<<< HEAD
using System;
using System.Globalization;

class URI {

    static void Main(string[] args) { 

        Console.Write("");
        string input_a = Console.ReadLine();
        int a = int.Parse(input_a);

        Console.Write("");
        string input_b = Console.ReadLine();
        int b = int.Parse(input_b);

        Console.Write("");
        string input_c = Console.ReadLine();
        double c = double.Parse(input_c, CultureInfo.InvariantCulture);

        double salary = b * c;

        Console.WriteLine($"NUMBER = {a}");
        Console.WriteLine($"SALARY = U$ {salary.ToString("F2", CultureInfo.InvariantCulture)}");

    }

=======
using System;
using System.Globalization;

class URI {

    static void Main(string[] args) { 

        Console.Write("");
        string input_a = Console.ReadLine();
        int a = int.Parse(input_a);

        Console.Write("");
        string input_b = Console.ReadLine();
        int b = int.Parse(input_b);

        Console.Write("");
        string input_c = Console.ReadLine();
        double c = double.Parse(input_c, CultureInfo.InvariantCulture);

        double salary = b * c;

        Console.WriteLine($"NUMBER = {a}");
        Console.WriteLine($"SALARY = U$ {salary.ToString("F2", CultureInfo.InvariantCulture)}");

    }

>>>>>>> 1cfb7856b5cd16d06c82bd088e56144c1fd011c8
}