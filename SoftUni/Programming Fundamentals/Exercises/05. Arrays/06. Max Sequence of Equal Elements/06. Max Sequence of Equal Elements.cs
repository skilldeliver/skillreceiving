using System;
using System.Linq;

namespace _06._Max_Sequence_of_Equal_Elements
{
    class Program
    {
        static void Main(string[] args)
        {
            long[] nums = Console.ReadLine().Split(' ').Select(long.Parse).ToArray();
            long start = 0;
            long len = 1;
            long bestLen = long.MinValue;
            long startLen = 0;

            for (int i = 1; i < nums.Length; i++)
            {
                if (nums[i] == nums[i - 1])
                {
                    len++;
                }
                else
                {
                    start = i;
                    len = 1;
                }

                if (len > bestLen)
                {
                    startLen = start;
                    bestLen = len;
                }
            }

            for (long i = startLen; i < startLen + bestLen; i++)
            {
                Console.Write(nums[i] + " ");
            }
        }
    }
}
