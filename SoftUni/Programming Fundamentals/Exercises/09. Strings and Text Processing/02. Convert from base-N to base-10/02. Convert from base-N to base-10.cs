using System;
using System.Linq;
using System.Numerics;

namespace _02._Convert_from_base_N_to_base_10
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] ns = Console.ReadLine().Split();
            BigInteger baseN = BigInteger.Parse(ns[0]);
            BigInteger num = BigInteger.Parse(ns[1]);
            Console.WriteLine(ConvertToBase10(num, baseN));
        }

        static BigInteger ConvertToBase10(BigInteger num, BigInteger baseN)
        {
            BigInteger result = new BigInteger();

            int i = 0;
            while (num > 0)
            {
                BigInteger n = num % 10;
                result += n * BigInteger.Pow(baseN, i);

                i++;
                num /= 10;
            }

            return result;
        }
    }
}