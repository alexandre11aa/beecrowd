<<<<<<< HEAD
using System;
using System.Globalization;

class URI {

    static void Main(string[] args) {

        string[] input_a = Console.ReadLine().Split(' ');
        string[] input_b = Console.ReadLine().Split(' ');
        
        double x_a = double.Parse(input_a[0], CultureInfo.InvariantCulture);
        double y_a = double.Parse(input_a[1], CultureInfo.InvariantCulture);
        
        double x_b = double.Parse(input_b[0], CultureInfo.InvariantCulture);
        double y_b = double.Parse(input_b[1], CultureInfo.InvariantCulture);

        double distance = (double)Math.Pow((x_a - x_b) * (x_a - x_b) + (y_a - y_b) * (y_a - y_b), 1.0/2);

        Console.WriteLine($"{distance.ToString("F4", CultureInfo.InvariantCulture)}");

    }      
=======
using System;
using System.Globalization;

class URI {

    static void Main(string[] args) {

        string[] input_a = Console.ReadLine().Split(' ');
        string[] input_b = Console.ReadLine().Split(' ');
        
        double x_a = double.Parse(input_a[0], CultureInfo.InvariantCulture);
        double y_a = double.Parse(input_a[1], CultureInfo.InvariantCulture);
        
        double x_b = double.Parse(input_b[0], CultureInfo.InvariantCulture);
        double y_b = double.Parse(input_b[1], CultureInfo.InvariantCulture);

        double distance = (double)Math.Pow((x_a - x_b) * (x_a - x_b) + (y_a - y_b) * (y_a - y_b), 1.0/2);

        Console.WriteLine($"{distance.ToString("F4", CultureInfo.InvariantCulture)}");

    }      
>>>>>>> 1cfb7856b5cd16d06c82bd088e56144c1fd011c8
}