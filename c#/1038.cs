using System; 
using System.Globalization;

class URI {

    static void Main(string[] args) { 

        string input_iq = Console.ReadLine();
        
        string[] iq = input_iq.Split(' ');
        
        int i = int.Parse(iq[0], CultureInfo.InvariantCulture);
        int q = int.Parse(iq[1], CultureInfo.InvariantCulture);
        
        double T;
        
        if (i == 1) {
            T = 4.00 * q;
        } else if (i == 2) {
            T = 4.50 * q;
        } else if (i == 3) {
            T = 5.00 * q;
        } else if (i == 4) {
            T = 2.00 * q;
        } else {
            T = 1.50 * q;
        }
        
        Console.WriteLine($"Total: R$ {T.ToString("F2", CultureInfo.InvariantCulture)}");

    }

}
