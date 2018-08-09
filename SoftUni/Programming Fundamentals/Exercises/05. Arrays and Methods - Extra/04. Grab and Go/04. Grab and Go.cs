using System;
using System.Linq;

namespace _04._Grab_and_Go
{
    class Program
    {
        static void Main(string[] args)
        {
            long[] nums = Console.ReadLine().Split(' ').Select(long.Parse).ToArray();
            long find = long.Parse(Console.ReadLine());
            long sum = 0;
            bool found = false;

            for (int i = 0; i < nums.Length; i++)
            {
                if (nums[i] == find)
                {
                    found = true;
                    sum = 0;
                    for (int j = i - 1; j >= 0; j--)
                    {
                        sum += nums[j];
                    }
                }
            }

            if (!found)
            {
                Console.WriteLine("No occurrences were found!");
                return;
            }

            Console.WriteLine(sum);
            
        }
    }
}
