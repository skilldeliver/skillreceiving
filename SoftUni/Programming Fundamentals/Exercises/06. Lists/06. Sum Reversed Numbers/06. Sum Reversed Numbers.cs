using System;
using System.Linq;

namespace _06._Sum_Reversed_Numbers
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] nums = Console.ReadLine().Split(' ');
            long sum = 0;

            for (int i = 0; i < nums.Length; i++)
            {
                long num = ReverseString(long.Parse(nums[i]));
                sum += num;
            }
            Console.WriteLine(sum);

        }

        static long ReverseString(long num)
        {
            long result = 0;

            while (num > 0)
            {
                long n = num % 10;
                Console.WriteLine(n);
                result = result * 10 + n;
                Console.WriteLine(result);
                num /= 10;
            }

            return result;
        }
    }
}
