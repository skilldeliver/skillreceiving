using System;
using System.Collections.Generic;
using System.Linq;


namespace _02._Append_Lists
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] input = Console.ReadLine().Split('|');

            List<int> nums = new List<int>();

            for (int i = input.Length - 1; i >= 0; i--)
            {
                foreach (string item in input[i].Trim().Split(' '))
                {
                    try
                    {
                        nums.Add(int.Parse(item));
                    }
                    catch (FormatException)
                    { }
                }
            }

            foreach(int item in nums)
            {
                Console.Write(item + " ");
            }
        }
    }
}
