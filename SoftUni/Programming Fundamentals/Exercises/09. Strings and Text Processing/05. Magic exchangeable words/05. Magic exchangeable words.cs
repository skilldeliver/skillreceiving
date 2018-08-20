using System;
using System.Linq;

namespace _05._Magic_exchangeable_words
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] tokens = Console.ReadLine().Split();
            string word1 = tokens[0];
            string word2 = tokens[1];

            if (word1.Distinct().ToArray().Length == word2.Distinct().ToArray().Length) Console.WriteLine("true");
            else Console.WriteLine("false");
        }
    }
}
