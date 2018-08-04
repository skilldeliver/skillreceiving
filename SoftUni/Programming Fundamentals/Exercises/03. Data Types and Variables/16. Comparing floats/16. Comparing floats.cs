using System;

namespace _16._Comparing_floats
{
    class Program
    {
        static void Main(string[] args)
        {
            decimal num1 = decimal.Parse(Console.ReadLine());
            decimal num2 = decimal.Parse(Console.ReadLine());

            Console.WriteLine(!(Math.Abs(num1 - num2) >= 0.000001m));
        }
    }
}
