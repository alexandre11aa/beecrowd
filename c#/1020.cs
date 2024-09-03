using System;

class URI {

    static void Main(string[] args) {

        string input_time = Console.ReadLine();

        int time = int.Parse(input_time);

        int year = time / 365;

        int mounth = (time - year * 365) / 30;

        int day = time - year * 365 - mounth * 30;

        Console.WriteLine($"{year} ano(s)\n{mounth} mes(es)\n{day} dia(s)");
        
    }    
}
