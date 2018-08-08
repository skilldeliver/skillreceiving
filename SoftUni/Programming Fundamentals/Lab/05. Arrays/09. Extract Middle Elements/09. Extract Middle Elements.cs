using System;
using System.Linq;

namespace _09._Extract_Middle_Elements
{
    class Program
    {
        static void Main(string[] args)
        {
            long[] nums = Console.ReadLine().Split(' ').Select(long.Parse).ToArray();
            long[] midElements = MidElementsOfArray(nums);
            PrintArr(midElements);
        }

        static long[] MidElementsOfArray(long[] arr)
        {
            int n = arr.Length;
            long[] newArr;

            if (arr.Length == 1)
            {
                newArr = new long[1];
                newArr[0] = arr[0];
            }
            else if (arr.Length % 2 == 0)
            {
                newArr = new long[2];
                newArr[0] = arr[n / 2 - 1];
                newArr[1] = arr[n / 2];
            }
            else
            {
                newArr = new long[3];
                newArr[0] = arr[n / 2 - 1];
                newArr[1] = arr[n / 2];
                newArr[2] = arr[n / 2 + 1];
            }

            return newArr;
        }

        static void PrintArr(long[] arr)
        {
            Console.Write("{ ");
            foreach (long item in arr)
            {
                Console.Write(item);
                if (!item.Equals(arr[arr.Length - 1]))
                {
                    Console.Write(", ");
                }
            }
            Console.Write(" }");
        }
    }
}
