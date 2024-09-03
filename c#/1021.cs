using System;

class URI {

    static void Main(string[] args) {

        string input_money = Console.ReadLine();

        string[] money = input_money.Split('.');
        
        int money_notas = (int)(double.Parse(money[0]));

        int money_moedas;

        if (money.Length > 1) {
            string money_moedas_str = "0." + money[1];
            money_moedas = (int)(double.Parse(money_moedas_str) * 10 * 10);
        } else {
            money_moedas = 0;
        }

        int n100 = money_notas / 100;

        int n50  = (money_notas - n100 * 100) / 50;

        int n20  = (money_notas - n100 * 100 - n50 * 50) / 20;

        int n10  = (money_notas - n100 * 100 - n50 * 50 - n20 * 20) / 10;

        int n5   = (money_notas - n100 * 100 - n50 * 50 - n20 * 20 - n10 * 10) / 5;

        int n2   = (money_notas - n100 * 100 - n50 * 50 - n20 * 20 - n10 * 10 - n5 * 5) / 2;

        int m100 = (money_notas - n100 * 100 - n50 * 50 - n20 * 20 - n10 * 10 - n5 * 5 - n2 * 2);

        int m50 = money_moedas / 50;

        int m25 = (money_moedas - m50 * 50) / 25;

        int m10 = (money_moedas - m50 * 50 - m25 * 25) / 10;

        int m5  = (money_moedas - m50 * 50 - m25 * 25 - m10 * 10) / 5;

        int m1  = (money_moedas - m50 * 50 - m25 * 25 - m10 * 10 - m5 * 5);

        Console.WriteLine($"NOTAS:");
        Console.WriteLine($"{n100} nota(s) de R$ 100.00");
        Console.WriteLine($"{n50} nota(s) de R$ 50.00");
        Console.WriteLine($"{n20} nota(s) de R$ 20.00");
        Console.WriteLine($"{n10} nota(s) de R$ 10.00");
        Console.WriteLine($"{n5} nota(s) de R$ 5.00");
        Console.WriteLine($"{n2} nota(s) de R$ 2.00");
        Console.WriteLine($"MOEDAS:");
        Console.WriteLine($"{m100} moeda(s) de R$ 1.00");
        Console.WriteLine($"{m50} moeda(s) de R$ 0.50");
        Console.WriteLine($"{m25} moeda(s) de R$ 0.25");
        Console.WriteLine($"{m10} moeda(s) de R$ 0.10");
        Console.WriteLine($"{m5} moeda(s) de R$ 0.05");
        Console.WriteLine($"{m1} moeda(s) de R$ 0.01");
        
    }    
}
