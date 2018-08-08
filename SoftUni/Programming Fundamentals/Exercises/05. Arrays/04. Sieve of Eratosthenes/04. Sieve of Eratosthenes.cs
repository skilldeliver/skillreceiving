using System;

namespace _04._Sieve_of_Eratosthenes
{
    class Program
    {
        static void Main(string[] args)
        {
            long n = long.Parse(Console.ReadLine());
            n++;

            bool[] primes = new bool[n];
            for (int i = 0; i < n; i++)
            {
                primes[i] = true;
            }

            primes[0] = false;
            primes[1] = false;


            for (int i = 1; i < Math.Sqrt(n); i++)
            {
                if (primes[i])
                {
                    for (int j = (int)Math.Pow(i, 2); j < n; j += i)
                    {
                        primes[j] = false;
                    }
                }
            }

            for (int i = 0; i < primes.Length; i++)
            {
                if (primes[i])
                {
                    Console.Write(i + " ");
                }
            }
        }
    }
}
