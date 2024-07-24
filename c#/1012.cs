using System;
using System.Globalization;

class URI {

    static void Main(string[] args) {

        string input = Console.ReadLine();
        string[] parts = input.Split(' ');
        
        double a = double.Parse(parts[0], CultureInfo.InvariantCulture);
        double b = double.Parse(parts[1], CultureInfo.InvariantCulture);
        double c = double.Parse(parts[2], CultureInfo.InvariantCulture);

        double triangulo = a * c / 2;
        double circulo = 3.14159 * c * c;
        double trapezio = (a + b) * c / 2;
        double quadrado = b * b;
        double retangulo = a * b;

        Console.WriteLine($"TRIANGULO: {triangulo.ToString("F3", CultureInfo.InvariantCulture)}");
        Console.WriteLine($"CIRCULO: {circulo.ToString("F3", CultureInfo.InvariantCulture)}");
        Console.WriteLine($"TRAPEZIO: {trapezio.ToString("F3", CultureInfo.InvariantCulture)}");
        Console.WriteLine($"QUADRADO: {quadrado.ToString("F3", CultureInfo.InvariantCulture)}");
        Console.WriteLine($"RETANGULO: {retangulo.ToString("F3", CultureInfo.InvariantCulture)}");

    }      
}