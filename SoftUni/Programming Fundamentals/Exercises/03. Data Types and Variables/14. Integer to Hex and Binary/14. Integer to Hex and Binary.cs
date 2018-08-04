using System;

namespace _14._Integer_to_Hex_and_Binary
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());

            Console.WriteLine(Convert.ToString(n, 16).ToUpper());
            Console.WriteLine(Convert.ToString(n, 2));
        }
    }
}
