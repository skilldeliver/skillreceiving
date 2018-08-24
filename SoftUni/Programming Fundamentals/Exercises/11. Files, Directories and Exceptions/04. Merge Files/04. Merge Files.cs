using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace _04._Merge_Files
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] nums1 = File.ReadAllLines(@"text1.txt");
            Dictionary<string, int> data = new Dictionary<string, int>();
            string[] nums2 = File.ReadAllLines(@"text2.txt");

            List<int> nums = new List<int>();

            foreach (string n in nums1)
            {
                nums.Add(int.Parse(n));
            }

            foreach (string n in nums2)
            {
                nums.Add(int.Parse(n));

            }
            nums = nums.OrderBy(x => x).ToList();

            File.WriteAllLines(@"output.txt", nums.Select(x => x.ToString()).ToArray());
            Console.WriteLine("Done!");
        }
    }
}
