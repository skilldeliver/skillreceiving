using System;
using System.Linq;

namespace _08._Most_Frequent_Number
{
    class Program
    {
        static void Main(string[] args)
        {
            long[] nums = Console.ReadLine().Split(' ').Select(long.Parse).ToArray();
            long max = long.MinValue;
            long num = 0;

            for (int i = 0; i < nums.Length; i++)
            {
                int count = 0;
                for (int j = 0; j < nums.Length; j++)
                {
                    if (j != i && nums[i] == nums[j])
                    {
                        count++;
                    }
                }

                if (count > max)
                {
                    max = count;
                    num = nums[i];
                }
            }

            Console.WriteLine(num);
        }
    }
}
