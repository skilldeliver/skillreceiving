using System;
using System.Linq;

namespace _11._Equal_Sums
{
    class Program
    {
        static void Main(string[] args)
        {

            string[] seq = Console.ReadLine().Split(' ');
            long[] nums = new long[seq.Length + 2];
            int j = 0;

            for (int i = 1; i <= seq.Length; i++, j++)
            {
                nums[i] = long.Parse(seq[j]);
            }

            for (int i = 1; i < nums.Length - 1; i++)
            {
                long leftSum = 0;
                long rightSum = 0;

                for (int k = 0; k < i; k++)
                {
                    leftSum += nums[k];
                }

                for (int k = i + 1; k < nums.Length; k++)
                {
                    rightSum += nums[k];
                }

                if (leftSum == rightSum)
                {
                    Console.WriteLine(i- 1);
                    return;
                }
            }

            Console.WriteLine("no");
        }


        static void PrintArr(long[] arr)
        {
            foreach (int i in arr)
            {
                Console.Write(i + " ");
            }
        }
    }
}
