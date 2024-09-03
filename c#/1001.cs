<<<<<<< HEAD
using System;

public class Soma {
    public int Somar(int x, int y) {
        return x + y;
    }
}

class Q2 {
    static void Main() {
        Soma sum = new Soma();

        Console.Write("");
        string input_a = Console.ReadLine();
        int a = int.Parse(input_a);

        Console.Write("");
        string input_b = Console.ReadLine();
        int b = int.Parse(input_b);

        Console.WriteLine("X = " + sum.Somar(a, b));
    }
}
=======
using System;

public class Soma {
    public int Somar(int x, int y) {
        return x + y;
    }
}

class Q2 {
    static void Main() {
        Soma sum = new Soma();

        Console.Write("");
        string input_a = Console.ReadLine();
        int a = int.Parse(input_a);

        Console.Write("");
        string input_b = Console.ReadLine();
        int b = int.Parse(input_b);

        Console.WriteLine("X = " + sum.Somar(a, b));
    }
}
>>>>>>> 1cfb7856b5cd16d06c82bd088e56144c1fd011c8
