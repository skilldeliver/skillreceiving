using System;
using System.Linq;

namespace _01._Array_Statistics
{
    class Program
    {
        static void Main(string[] args)
        {
            long[] nums = Console.ReadLine().Split(' ').Select(long.Parse).ToArray();

            long min = long.MaxValue;
            long max = long.MinValue;
            long sum = 0;

            for (int i = 0; i < nums.Length; i++)
            {
                if (nums[i] < min)
                {
                    min = nums[i];
                }

                if (nums[i] > max)
                {
                    max = nums[i];
                }

                sum += nums[i];
            }
            double avg = (double)sum / (double)nums.Length;

            Console.WriteLine("Min = " + min + "\nMax = " + max + "\nSum = " + sum + "\nAvarage = " + avg);

        }
    }
}
