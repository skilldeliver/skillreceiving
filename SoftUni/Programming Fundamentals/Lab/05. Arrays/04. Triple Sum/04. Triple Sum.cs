using System;
using System.Linq;

namespace _04._Triple_Sum
{
    class Program
    {
        static void Main(string[] args)
        {

            long[] nums = Console.ReadLine().Split(' ').Select(long.Parse).ToArray();
            int n = nums.Length;
            bool exist = false;

            for (int a = 0; a < n; a++)
            {
                for (int b = a + 1; b < n; b++)
                {
                    long sum = nums[a] + nums[b];
                    
                    if (nums.Contains(sum))
                    {
                        Console.WriteLine(nums[a] + " + " + nums[b] + " == " + sum);
                        exist = true;
                    }
                }
            }

            if (!exist) Console.WriteLine("No");
        }
    }
}
