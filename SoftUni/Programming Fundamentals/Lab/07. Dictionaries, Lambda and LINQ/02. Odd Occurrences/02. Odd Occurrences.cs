using System;
using System.Collections.Generic;
using System.Linq;

namespace _02._Odd_Occurrences
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] line = Console.ReadLine().ToLower().Split(' ');

            Dictionary<string, int> dict = new Dictionary<string, int>();

            foreach (string word in line)
            {
                if (dict.ContainsKey(word))
                {
                    dict[word] += 1;
                }
                else
                {
                    dict[word] = 1;
                }
            }

            List<string> results = new List<string>();

            foreach (var entry in dict)
            {
                if (entry.Value % 2 != 0)
                {
                    results.Add(entry.Key);
                }
            }

            Console.WriteLine(string.Join(", ", results));

        }
    }
}
