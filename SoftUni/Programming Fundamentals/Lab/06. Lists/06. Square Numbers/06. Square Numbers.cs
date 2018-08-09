using System;
using System.Linq;
using System.Collections.Generic;

namespace _06._Square_Numbers
{
    class Program
    {
        static void Main(string[] args)
        {
            List<decimal> nums = Console.ReadLine().Split(' ').Select(decimal.Parse).ToList();
            List<decimal> squareNums = new List<decimal>();

            foreach (decimal n in nums)
            {

                if (Math.Sqrt((double)n) == (int)Math.Sqrt((double)n))
                {
                    squareNums.Add(n);
                }
            }
            squareNums.Sort((a, b) => b.CompareTo(a));

            foreach (decimal n in squareNums)
            {
                Console.Write(n + " ");
            }

        }
    }
}
