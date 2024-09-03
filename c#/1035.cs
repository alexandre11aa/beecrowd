using System;

class URI {

    static void Main(string[] args) {

        string input_abcd = Console.ReadLine();

        string[] abcd = input_abcd.Split(' ');

        int a = int.Parse(abcd[0]);
        int b = int.Parse(abcd[1]);
        int c = int.Parse(abcd[2]);
        int d = int.Parse(abcd[3]);
                
        if ((b > c) && (d > a) && ((c + d) > (a + b)) && (c >= 0) && (d >= 0) && (a % 2 == 0)){
            Console.WriteLine("Valores aceitos");
        } else {
            Console.WriteLine("Valores nao aceitos");
        }
    }    
}
