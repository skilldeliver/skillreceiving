using System;

namespace _02._Add_Two_Numbers
{
    class Program
    {
        static void Main(string[] args)
        {
            int num_1 = int.Parse(Console.ReadLine());
            int num_2 = int.Parse(Console.ReadLine());

            int sum = num_1 + num_2;
            Console.WriteLine($"{num_1} + {num_2} = {sum}");

        }
    }
}
