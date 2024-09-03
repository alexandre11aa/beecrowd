using System;
using System.Globalization;

class URI {

    static void Main(string[] args) {

        string input_abcd = Console.ReadLine();

        string[] abc = input_abcd.Split(' ');

        double a = double.Parse(abc[0], CultureInfo.InvariantCulture);
        double b = double.Parse(abc[1], CultureInfo.InvariantCulture);
        double c = double.Parse(abc[2], CultureInfo.InvariantCulture);

        double delta = b * b - 4 * a * c;
                
        if ((a == 0) || (delta < 0)){
            Console.WriteLine("Impossivel calcular");
        } else {
            double x1 = (- b + Math.Sqrt(delta)) / (2 * a);
            double x2 = (- b - Math.Sqrt(delta)) / (2 * a);

            Console.WriteLine($"R1 = {x1.ToString("F5", CultureInfo.InvariantCulture)}");
            Console.WriteLine($"R2 = {x2.ToString("F5", CultureInfo.InvariantCulture)}");
        }
    }    
}
