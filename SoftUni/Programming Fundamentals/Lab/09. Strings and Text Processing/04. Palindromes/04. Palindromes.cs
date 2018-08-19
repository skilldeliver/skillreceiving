using System;
using System.Linq;
using System.Collections.Generic;


namespace _04._Palindromes
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] words = Console.ReadLine().Split(" ,.?!".ToCharArray(), StringSplitOptions.RemoveEmptyEntries);
            List<string> palindromes = new List<string>();

            foreach (string word in words)
            {
                if (word == string.Join("", word.ToArray().Reverse()))
                {
                    palindromes.Add(word);
                }
            }
            Console.WriteLine(string.Join(", ", palindromes.Distinct().OrderBy(p => p)));
        }
    }
}
