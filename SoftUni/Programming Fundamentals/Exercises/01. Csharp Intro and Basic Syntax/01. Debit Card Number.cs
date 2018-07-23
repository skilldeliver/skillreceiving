using System;

namespace _01._CSharp_Intro_and_Basic_Syntax__Exercises
{
    class Program
    {
        static void Main(string[] args)
        {
            int num_1 = int.Parse(Console.ReadLine());
            int num_2 = int.Parse(Console.ReadLine());
            int num_3 = int.Parse(Console.ReadLine());
            int num_4 = int.Parse(Console.ReadLine());


            Console.WriteLine($"{num_1:d4} {num_2:d4} {num_3:d4} {num_4:d4}");
        }
    }
}
