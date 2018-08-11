using System;
using System.Collections.Generic;

namespace _07._Dictionaries__Lambda_and_LINQ___Lab
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] realNumbers = Console.ReadLine().Split(' ');
            SortedDictionary<double, int> dict = new SortedDictionary<double, int>();

            foreach (string num in realNumbers)
            {
                if (dict.ContainsKey(double.Parse(num)))
                {
                    dict[double.Parse(num)] += 1;
                }
                else
                {
                    dict[double.Parse(num)] = 1;
                }
            }
            
            foreach (KeyValuePair<double, int> entry in dict)
            {
                Console.WriteLine(entry.Key + " -> " + entry.Value);
            }
        }
    }
}
