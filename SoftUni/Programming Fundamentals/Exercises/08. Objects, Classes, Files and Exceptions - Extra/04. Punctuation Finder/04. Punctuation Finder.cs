using System;
using System.Collections.Generic;
using System.IO;

namespace _04._Punctuation_Finder
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] lines = File.ReadAllLines(@"sample.txt");
            string chars = ".,!?:";
            List<char> charArr = new List<char>();

            foreach (string line in lines)
            {
                foreach (char chr in line)
                {
                    if (chars.IndexOf(chr) != -1)
                    {
                        charArr.Add(chr);
                    }
                }
            }

            Console.WriteLine(string.Join(", ", charArr));
        }
    }
}
