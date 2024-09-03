using System;
using System.Globalization;

class URI {

    static void Main(string[] args) {

        double result = 0.0;
        
        int i = 0;

        while (i < 2) {

            Console.Write("");
            string input = Console.ReadLine();

            string[] parts = input.Split(' ');

            int b = int.Parse(parts[1]);
            double c = double.Parse(parts[2], CultureInfo.InvariantCulture);

            result += b * c; 

            i++;

        }      

        Console.WriteLine($"VALOR A PAGAR: R$ {result.ToString("F2", CultureInfo.InvariantCulture)}");

    }

}