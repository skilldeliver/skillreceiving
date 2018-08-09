using System;
using System.Linq;

namespace _09._Jump_Around
{
    class Program
    {
        static void Main(string[] args)
        {
            long[] nums = Console.ReadLine().Split(' ').Select(long.Parse).ToArray();

            bool possible = true;
            long sum = 0;
            long index = 0;


            while (possible)
            {
                sum += nums[index];
                long try1 = index + nums[index];
                long try2 = index - nums[index];

                if (try1 < nums.Length)
                {
                    index = try1;
                }
                else if (try2 > 0)
                {
                    index = try2;
                }
                else
                {
                    possible = false;
                }
            }

            Console.WriteLine(sum);
            
        }
    }
}
