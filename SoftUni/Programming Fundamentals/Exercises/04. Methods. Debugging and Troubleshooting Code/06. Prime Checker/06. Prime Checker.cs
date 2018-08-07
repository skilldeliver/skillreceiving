using System;

namespace _06._Prime_Checker
{
    class Program
    {
        static void Main(string[] args)
        {
            double n = double.Parse(Console.ReadLine());
            Console.WriteLine(IsPrime(n));
        }

        static bool IsPrime(double num) 
        {
            long n = (long)Math.Round(num);
            if (n == 0 || n == 1) return false;

            for (int i = 2; i <= Math.Sqrt(n); i++)
            {
                if (n % i == 0) return false;
            }

            return true;

        }

    }
}
