using System;

namespace _09._Multiply_Evens_by_Odds
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            Console.WriteLine(GetMultipleOfEvensAndOdds(n));
        }

        private static int GetMultipleOfEvensAndOdds(int n)
        {
            n = Math.Abs(n);
            int sumEvens = GetSumOfEvensDigits(n);
            int sumOdds = GetSumOfOddDigits(n);
            return sumEvens * sumOdds;

        }

        private static int GetSumOfEvensDigits(int n)
        {
            int sum = 0;

            while (n > 0)
            {
                int lastDigit = n % 10;
                if (lastDigit % 2 == 0)
                {
                    sum += lastDigit;
                }
                n /= 10;
            }

            return sum;
        }

        private static int GetSumOfOddDigits(int n)
        {
            int sum = 0;

            while (n > 0)
            {
                int lastDigit = n % 10;
                if (lastDigit % 2 != 0)
                {
                    sum += lastDigit;
                }
                n /= 10;
            }

            return sum;
        }


    }
}
