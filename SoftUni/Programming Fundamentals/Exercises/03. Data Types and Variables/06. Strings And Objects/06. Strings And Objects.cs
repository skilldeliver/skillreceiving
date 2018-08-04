using System;

namespace _06._Strings_And_Objects
{
    class Program
    {
        static void Main(string[] args)
        {
            string word1 = Console.ReadLine();
            string word2 = Console.ReadLine();

            object concat = word1 + " " + word2;
            string output = (string)concat;

            Console.WriteLine(output);
        }
    }
}
