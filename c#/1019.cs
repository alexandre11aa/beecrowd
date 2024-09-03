using System;

class URI {

    static void Main(string[] args) {

        string input_time = Console.ReadLine();

        int time = int.Parse(input_time);

        int hour = time / 3600;

        int minute = (time - hour * 3600) / 60;

        int second = time - hour * 3600 - minute * 60;

        Console.WriteLine($"{hour}:{minute}:{second}");
        
    }    
}
