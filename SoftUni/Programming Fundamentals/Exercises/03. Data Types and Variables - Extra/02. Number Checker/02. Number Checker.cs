using System;

namespace _02._Number_Checker
{
    class Program
    {
        static void Main(string[] args)
        {
            string input = Console.ReadLine();

            for (int i = 0; i < input.Length; i++)
            {
                if (input[i] + "" == ".")
                {
                    Console.WriteLine("floating-point");
                    return;
                }
            }
            Console.WriteLine("integer");
        }
    }
}
