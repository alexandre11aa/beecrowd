using System;
using System.Globalization;

class Calcular {
    public double Area_do_Circulo(double r) {
        return 3.14159 * r * r;
    }
}

class Q3 {
    static void Main() {
        Calcular calc = new Calcular();

        Console.Write("");
        string input_r = Console.ReadLine();
        double r = double.Parse(input_r);

        string raio = calc.Area_do_Circulo(r).ToString("0.0000", CultureInfo.InvariantCulture);

        Console.WriteLine($"A={raio}");
    }

}