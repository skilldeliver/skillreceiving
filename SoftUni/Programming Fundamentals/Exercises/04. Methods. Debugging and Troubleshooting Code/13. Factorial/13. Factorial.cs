using System;
using System.Numerics;

namespace _13._Factorial
{
    class Program
    {
        static void Main(string[] args)
        {
            int num = int.Parse(Console.ReadLine());
            Console.WriteLine(Factorial(num));
        }

        static BigInteger Factorial(int num)
        {
            BigInteger factorial = 1;
            for (int i = 1; i <= num; i++)
            {
                factorial *= i;
            }

            return factorial;
        }
    }
}
