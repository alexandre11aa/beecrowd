using System;

class URI {

    static void Main(string[] args) {

        string[] inputs = Console.ReadLine().Split(' ');
        
        int a = int.Parse(inputs[0]);
        int b = int.Parse(inputs[1]);
        int c = int.Parse(inputs[2]);

        int relative = (a + b + Math.Abs(a - b)) / 2;
        int absolute = (relative + c + Math.Abs(relative - c)) / 2;

        Console.WriteLine(absolute + " eh o maior");

    }      
}