using System;
using System.Numerics;

namespace _03._Big_Factorial
{
    class Program
    {
        static void Main(string[] args)
        {

            BigInteger fact = 1;
            long n = long.Parse(Console.ReadLine());

            for (int i = 2; i <= n; i++)
            {
                fact *= i;
            }
            Console.WriteLine(fact);
        }
    }
}
