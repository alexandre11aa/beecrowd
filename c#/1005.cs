using System;
using System.Globalization;

class Calcular {
    public double Media(double x, double y) {
        return (x * 3.5 + y * 7.5) / 11;
    }
}

class Q6 {
    static void Main() {
        Calcular med = new Calcular();

        Console.Write("");
        string input_a = Console.ReadLine();
        double a = double.Parse(input_a, CultureInfo.InvariantCulture);

        Console.Write("");
        string input_b = Console.ReadLine();
        double b = double.Parse(input_b, CultureInfo.InvariantCulture);

        string result = med.Media(a, b).ToString("F5", CultureInfo.InvariantCulture);

        Console.WriteLine($"MEDIA = {result}");
    }
}