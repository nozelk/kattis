using System;

class Program
{
    static void Main()
    {
        // Read input
        string[] input = Console.ReadLine().Split();
        int R1 = int.Parse(input[0]);
        int S = int.Parse(input[1]);

        // Calculate R2
        int R2 = 2 * S - R1;

        // Output the result
        Console.WriteLine(R2);
    }
}
