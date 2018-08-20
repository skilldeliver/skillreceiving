using System;
using System.Numerics;

namespace _09._Strings_and_Text_Processing___Exercises
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] ns = Console.ReadLine().Split();
            long baseN = long.Parse(ns[0]);
            BigInteger num = BigInteger.Parse(ns[1]);

            Console.WriteLine(baseConverter(num, baseN));
        }

        static string baseConverter(BigInteger num, long baseN)
        {
            string digits = "0123456789ABCDEF";
            string newString = "";

            while (num > 0)
            {
                long rem =(long)(num % baseN);
                newString = digits[(int)rem] + newString;
                num /= baseN;
            }

            return newString;
        }
    }
}
