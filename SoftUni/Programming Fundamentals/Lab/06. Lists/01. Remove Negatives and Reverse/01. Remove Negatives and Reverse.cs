using System;
using System.Linq;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        List<int> nums = Console.ReadLine().Split(' ').Select(int.Parse).ToList();
        bool empty = true;

        for (int i = nums.Count - 1; i >= 0; i--)
        {
            if (nums[i] >= 0)
            {
                empty = false;
                Console.Write(nums[i] + " ");
            }
        }

        if (empty) Console.WriteLine("empty");
    }

}

