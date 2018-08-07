using System;
using System.Collections.Generic;

namespace _07._Primes_in_Given_Range
{
    class Program
    {
        static void Main(string[] args)
        {
            int startNum = int.Parse(Console.ReadLine());
            int endNum = int.Parse(Console.ReadLine());

            List<int> primes = FindPrimesInRange(startNum, endNum);
            int last = primes[primes.Count - 1];

            foreach (int element in FindPrimesInRange(startNum, endNum))
            {
                if (element.Equals(last)) Console.Write(element);
                else Console.Write(element + ", ");
            }
            
        }

        static List<int> FindPrimesInRange(int startNum, int endNum)
        {
            List<int> primes = new List<int>();

            for (int i = startNum; i <= endNum; i++)
            {
                if (IsPrime(i)) primes.Add(i);

            }

            return primes;
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
