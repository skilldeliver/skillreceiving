using System;
using System.Collections.Generic;

namespace _04._Split_by_Word_Casing
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] words = Console.ReadLine().Split(new char[] { ' ', ',', ';', ':', '.', '!', '(', ')', '"', '\'', '\\', '/', '[', ']'}, StringSplitOptions.RemoveEmptyEntries);

            List<string> lowerCase = new List<string>();
            List<string> upperCase = new List<string>();
            List<string> mixedCase = new List<string>();

            foreach (string word in words)
            {
                int upper = 0;
                int lower = 0;


                foreach (char chr in word)
                {
                    if (Char.IsUpper(chr))
                    {
                        upper += 1;
                    }
                    else if (Char.IsLower(chr))
                    {
                        lower += 1;
                    }
                }

                if (lower == word.Length)
                {
                    lowerCase.Add(word);
                }
                else if (upper == word.Length)
                {
                    upperCase.Add(word);
                }
                else
                {
                    mixedCase.Add(word);
                }
                
            }

            Console.Write("Lower-case: ");
            PrintList(lowerCase);
            Console.Write("Mixed-case: ");
            PrintList(mixedCase);
            Console.Write("Upper-case: ");
            PrintList(upperCase);

        }

        static void PrintList(List<string> list)
        {
            for (int i = 0; i < list.Count - 1; i++)
            {
                Console.Write(list[i] + ", ");
            }
            Console.WriteLine(list[list.Count - 1]);

        }
    }
}
