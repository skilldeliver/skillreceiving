using System;
using System.Collections.Generic;
using System.Linq;

namespace _06._Lists___Exercises
{
    class Program
    {
        static void Main(string[] args)
        {

            List<long> nums = Console.ReadLine().Split(' ').Select(long.Parse).ToList();

            int start = 0;
            int len = 1;
            int bestStart = 0;
            int bestLen = 1;

            for (int i = 1; i < nums.Count; i++)
            {
                if (nums[i] == nums[i - 1])
                {
                    len += 1;
                }
                else
                {
                    start = i;
                    len = 1;
                }

                if (len > bestLen)
                {
                    bestStart = start;
                    bestLen = len;
                }
            }

            for (int i = bestStart; i < bestStart + bestLen; i++)
            {
                Console.Write(nums[i] + " ");
            }

        }
    }
}
