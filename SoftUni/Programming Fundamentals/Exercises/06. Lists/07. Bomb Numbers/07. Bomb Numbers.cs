using System;
using System.Linq;
using System.Collections.Generic;

namespace _07._Bomb_Numbers
{
    class Program
    {
        static void Main(string[] args)
        {
            List<long> nums = Console.ReadLine().Split(' ').Select(long.Parse).ToList();
            List<int> bombPower = Console.ReadLine().Split(' ').Select(int.Parse).ToList();

            for (int i = 0; i < nums.Count; i++)
            {
                if (nums[i] == bombPower[0])
                {
                    int startPoint = i - bombPower[1];
                    int endPoint = i + bombPower[1];
                    if (startPoint < 0) startPoint = 0;
                    if (endPoint > nums.Count - 1) endPoint = nums.Count - 1;

                    for (int j = startPoint; j < i; j++)
                    {
                        nums[j] = 0;
                    }
                    for (int j = i; j <= endPoint; j++)
                    {
                        nums[j] = 0;
                    }
                }
            }
            long sum = 0;

            foreach (long item in nums)
            {
                sum += item;
            }
            Console.WriteLine(sum);
        }
    }
}
