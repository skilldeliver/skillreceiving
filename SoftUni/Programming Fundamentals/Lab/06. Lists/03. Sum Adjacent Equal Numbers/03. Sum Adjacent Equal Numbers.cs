using System;
using System.Collections.Generic;
using System.Linq;

namespace _03._Sum_Adjacent_Equal_Numbers
{
    class Program
    {
        static void Main(string[] args)
        {
            List<decimal> nums = Console.ReadLine().Split(' ').Select(decimal.Parse).ToList();

            bool more = true;
            while (more)
            {
                more = false;
                for (int i = 0; i < nums.Count - 1; i++)
                {
                    if (nums[i] == nums[i + 1])
                    {
                        more = true;
                        nums[i] = nums[i] + nums[i + 1];
                        nums.RemoveAt(i + 1);
                    }
                }
            }

            foreach(decimal item in nums)
            {
                Console.Write(item + " ");
            }
        }
    }
}
