using System;
using System.Linq;

namespace _10._Pairs_by_Difference
{
    class Program
    {
        static void Main(string[] args)
        {
            long[] nums = Console.ReadLine().Split(' ').Select(long.Parse).ToArray();
            long diff = long.Parse(Console.ReadLine());
            int count = 0;

            for (int i = 0; i < nums.Length; i++)
            {
                for (int j = 0; j < nums.Length; j++)
                {
                    if (Math.Abs(nums[i] - nums[j]) == diff)
                    {
                        count += 1;
                    }
                }
            }

            Console.WriteLine(count / 2);

        }
    }
}
