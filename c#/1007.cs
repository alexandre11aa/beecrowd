using System;

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
        int c = int.Parse(input_c);

        Console.Write("");
        string input_d = Console.ReadLine();
        int d = int.Parse(input_d);

        Console.WriteLine($"DIFERENCA = {a * b - c * d}");

    }

}