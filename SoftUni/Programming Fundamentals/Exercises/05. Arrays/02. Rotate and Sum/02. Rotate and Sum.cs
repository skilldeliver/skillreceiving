using System;
using System.Linq;

namespace _02._Rotate_and_Sum
{
    class Program
    {
        static void Main(string[] args)
        {
            long[] nums = Console.ReadLine().Split(' ').Select(long.Parse).ToArray();
            int k = int.Parse(Console.ReadLine());
            long[] sumArr = new long[nums.Length];

            for (int i = 0; i < k; i++)
            {
                nums = Rshift(nums);
                for (int j = 0; j < nums.Length; j++)
                {
                    sumArr[j] += nums[j];
                }
            }

            PrintArr(sumArr);


        }

        static long[] Rshift(long[] arr)
        {
            long lastElement = arr[arr.Length - 1];

            for (int i = arr.Length - 1; i >= 1; i--)
            {
                arr[i] = arr[i - 1];
            }

            arr[0] = lastElement;
            return arr;
        }

        static void PrintArr(long[] arr)
        {
            foreach (long item in arr)
            {
                Console.Write(item + " ");
            }
        }
    }
}
