using System;
using System.Linq;
using System.Collections.Generic;

namespace _05._Sort_Numbers
{
    class Program
    {
        static void Main(string[] args)
        {
            List<decimal> nums = Console.ReadLine().Split(' ').Select(decimal.Parse).ToList();
            nums.Sort();

            for (int i = 0; i < nums.Count; i++)
            {
                Console.Write(nums[i]);
                if (i != nums.Count - 1)
                {
                    Console.Write(" <= ");
                }
                
            }
        }
    }
}
