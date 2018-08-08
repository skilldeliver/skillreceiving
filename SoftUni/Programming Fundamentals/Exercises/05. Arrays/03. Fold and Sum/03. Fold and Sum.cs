using System;
using System.Linq;
using System.Collections;

namespace _03._Fold_and_Sum
{
    class Program
    {
        static void Main(string[] args)
        {
            long[] nums = Console.ReadLine().Split(' ').Select(long.Parse).ToArray();

            int k = nums.Length;
            int index = k / 4;

            long[] firstPart = new long[index];

            for (int i = 0; i < index; i++)
            {
                firstPart[i] = nums[i];
            }

            long[] secondPart = new long[index];

            int j = 0;
            for (int i = nums.Length - index; i < nums.Length; i++, j++)
            {
                secondPart[j] = nums[i];
            }

            firstPart = Reverse(firstPart);
            secondPart = Reverse(secondPart);

            long[] firstRow = FirstRow(firstPart, secondPart);

            long[] secondRow = new long[index * 2];

            j = 0;
            for (int i = index; i < nums.Length - index; i++, j++)
            {
                secondRow[j] = nums[i];
            }

            long[] sumArray = SumArrays(firstRow, secondRow);
            PrintArr(sumArray);
            

        }

        static long[] SumArrays(long[] arr1, long[] arr2)
        {
            long[] newArr = new long[arr1.Length];

            for (int i = 0; i < arr1.Length; i++)
            {
                newArr[i] = arr1[i] + arr2[i];
            }

            return newArr;
        }

        static long[] FirstRow(long[] arr1, long[] arr2)
        {
            long[] firstRow = new long[arr1.Length + arr2.Length];
            arr1.CopyTo(firstRow, 0);
            arr2.CopyTo(firstRow, arr1.Length);

            return firstRow;
        }

        static void PrintArr(long[] arr)
        {
            foreach (long item in arr)
            {
                Console.Write(item + " ");
            }
        }

        static long[] Reverse(long[] arr)
        {
            long[] newArr = new long[arr.Length];

            int j = 0;
            for (int i = arr.Length - 1; i >= 0; i--, j++)
            {
                newArr[j] = arr[i];
            }

            return newArr;
        }
    }
}
