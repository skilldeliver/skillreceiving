using System;
using System.Linq;
using System.Collections.Generic;

namespace _02._Odd_Filter
{
    class Program
    {
        static void Main(string[] args)
        {
            long[] nums = Console.ReadLine().Split(' ').Select(long.Parse).ToArray();

            List<long> evens = new List<long>();

            foreach (long n in nums)
            {
                if (n % 2 == 0) evens.Add(n);
            }

            double avg = evens.Average();

            for (int i = 0; i < evens.Count; i++)
            {
                if (evens[i] > avg) evens[i] += 1;
                else evens[i] -= 1;
            }

            Console.WriteLine(string.Join(" ", evens));
        }
    }
}
