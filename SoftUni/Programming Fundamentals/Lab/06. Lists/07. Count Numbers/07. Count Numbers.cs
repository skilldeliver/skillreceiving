using System;
using System.Linq;
using System.Collections.Generic;

namespace _07._Count_Numbers
{
    class Program
    {
        static void Main(string[] args)
        {

            List<long> nums = Console.ReadLine().Split(' ').Select(long.Parse).ToList();
            Dictionary<long, long> dictionary = new Dictionary<long, long>();
            nums.Sort();

            for (int i = 0; i < nums.Count; i++)
            {
                try
                {
                    dictionary[nums[i]] += 1;
                }
                catch (KeyNotFoundException)
                {
                    dictionary.Add(nums[i], 1);
                }
            }

            foreach (KeyValuePair<long, long> entry in dictionary)
            {
                Console.WriteLine(entry.Key + " -> " + entry.Value);
            }
        }
    }
}
