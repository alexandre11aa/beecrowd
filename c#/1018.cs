using System;

class URI {

    static void Main(string[] args) {

        int n100 = 0, n50 = 0, n20 = 0, n10 = 0, n5 = 0, n2 = 0, n1 = 0;

        string input_a = Console.ReadLine();

        int a = int.Parse(input_a);

        Console.WriteLine(a);

        while (true) {
            if (a == 0) {
                break;
            }

            if (a >= 100) {
                double n_temp = a / 100.0;
                string n_temp_str = n_temp.ToString();
                string[] parts = n_temp_str.Split('.');

                n100 += (int)(double.Parse(parts[0]));

                if (parts.Length > 1) {
                    a = (int)(double.Parse(parts[1]));
                } else {
                    a = 0;
                } 

            } else if (a >= 50) {
                n50 += 1;
                a -= 50; 

            } else if (a >= 20) {
                n20 += 1;
                a -= 20; 

            } else if (a >= 10) {
                n10 += 1;
                a -= 10; 

            } else if (a >= 5) {
                n5 += 1;
                a -= 5;  

            } else if (a >= 2) {
                n2 += 1;
                a -= 2;

            } else {
                n1 += 1;
                a -= 1;  
            }
        }

        Console.WriteLine($"{n100} nota(s) de R$ 100,00");
        Console.WriteLine($"{n50} nota(s) de R$ 50,00");
        Console.WriteLine($"{n20} nota(s) de R$ 20,00");
        Console.WriteLine($"{n10} nota(s) de R$ 10,00");
        Console.WriteLine($"{n5} nota(s) de R$ 5,00");
        Console.WriteLine($"{n2} nota(s) de R$ 2,00");
        Console.WriteLine($"{n1} nota(s) de R$ 1,00");

    }    
}
