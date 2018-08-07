using System;
using System.Numerics;

namespace _14._Factorial_Trailing_Zeroes
{
    class Program
    {
        static void Main(string[] args)
        {
            int num = int.Parse(Console.ReadLine());
            Console.WriteLine(TrailingZeros(Factorial(num)));
        }
        static long TrailingZeros(BigInteger num)
        {
            string strNum = num.ToString();
            long count = 0;

            for (int i = strNum.Length - 1; i >= 0; i--)
            {
                if (strNum[i] + "" == "0") count++;
                else break;
            }

            return count;
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
