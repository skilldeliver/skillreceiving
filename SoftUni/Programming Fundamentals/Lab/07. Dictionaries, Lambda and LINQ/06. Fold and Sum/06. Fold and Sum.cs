using System;
using System.Linq;

namespace _06._Fold_and_Sum
{
    class Program
    {
        static void Main(string[] args)
        {
            long[] nums = Console.ReadLine().Split(' ').Select(long.Parse).ToArray();
            long[] row1 = nums.Take(nums.Length / 4).Reverse().ToArray().Concat(nums.Skip(nums.Length - nums.Length / 4).Reverse().ToArray()).ToArray();
            long[] row2 = nums.Skip(nums.Length / 4).Take(nums.Length / 2).ToArray();
            long[] sum = row1.Select((x, index) => x + row2[index]).ToArray();
            Console.WriteLine(string.Join(" ", sum));
        }
    }
}
