using System;
using System.Linq;

namespace _08._Condense_Array_to_Number
{   
    class Program
    {
        static void Main(string[] args)
        {

            long[] nums = Console.ReadLine().Split(' ').Select(long.Parse).ToArray();
            
            while (nums.Length > 1)
            {
                long[] condensed = new long[nums.Length - 1];

                for (int i = 0; i < nums.Length - 1; i++)
                {
                    condensed[i] = nums[i] + nums[i + 1];
                }

                nums = condensed;
            }
            PrintArr(nums);
        }
        static void PrintArr(long[] arr)
        {
            foreach (long item in arr)
            {
                Console.Write(item);
            }
        }
    }
}
