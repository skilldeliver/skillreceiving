using System;
using System.Collections.Generic;
using System.Linq;

namespace _04._Longest_Increasing_Subsequence
{
    class Program
    {
        static void Main(string[] args)
        {
            var nums = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
            var longestSeq = FindLongestIncreasingSubsequence(nums);
            Console.WriteLine(string.Join(" ", longestSeq));
        }

        public static int[] FindLongestIncreasingSubsequence(int[] nums)
        {
            int[] len = new int[nums.Length];
            int[] prev = new int[nums.Length];
            int maxLen = 0;
            int left = -1;

            for (int i = 0; i < nums.Length; i++)
            {
                len[i] = 1;
                prev[i] = -1;

                for (int j = 0; j < i; j++)
                {
                    if (nums[j] < nums[i] && len[j] >= len[i])
                    {
                        len[i] = 1 + len[j];
                        prev[i] = j;
                    }
                }

                if (len[i] > maxLen)
                {
                    maxLen = len[i];
                    left = i;
                }
            }

            var longestSeq = new List<int>();
            for (int i = 0; i < maxLen; i++)
            {
                longestSeq.Add(nums[left]);
                left = prev[left];
            }

            longestSeq.Reverse();
            return longestSeq.ToArray();
        }
    }
}

