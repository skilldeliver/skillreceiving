using System;
using System.Linq;

namespace _07._Sum_Arrays
{
    class Program
    {
        static void Main(string[] args)
        {
            long[] arr1 = Console.ReadLine().Split(' ').Select(long.Parse).ToArray();
            long[] arr2 = Console.ReadLine().Split(' ').Select(long.Parse).ToArray();

            int max = Max(arr1.Length, arr2.Length);

            long[] sums = new long[max];

            for (int i = 0; i < max; i++)
            {
                sums[i] += arr1[i % arr1.Length] + arr2[i % arr2.Length];
            }

            PrintArr(sums);

        }

        static void PrintArr(long[] arr)
        {
            foreach (long item in arr)
            {
                Console.Write(item + " ");
            }
        }

        static int Max(int len1, int len2)
        {
            if (len1 >= len2) return len1;
            return len2;
        }
    }
}
