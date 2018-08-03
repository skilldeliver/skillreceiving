using System;

namespace _03._Exact_Sum_of_Real_Numbers
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());

            decimal total = 0;
            for (int i = 0; i < n; i++)
            {
                total += decimal.Parse(Console.ReadLine());
            }
            Console.WriteLine(total);
        }
    }
}
