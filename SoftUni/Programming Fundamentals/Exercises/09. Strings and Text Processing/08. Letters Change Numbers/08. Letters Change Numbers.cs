using System;

namespace _08._Letters_Change_Numbers
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] words = Console.ReadLine().Split();
            double total = 0;
            string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

            foreach (string w in words)
            {
                if (string.IsNullOrWhiteSpace(w)) continue;
                string word = w.Trim();
                double num = double.Parse(word.Substring(1, word.Length - 2));
                
                if (char.IsUpper(word[0]))
                {
                    num /= alphabet.IndexOf(word[0]) + 1;
                }
                else
                {
                    num *= alphabet.ToLower().IndexOf(word[0]) + 1;
                }

                if (char.IsUpper(word[word.Length - 1]))
                {
                    num -= alphabet.IndexOf(word[word.Length - 1]) + 1;
                }
                else
                {
                    num += alphabet.ToLower().IndexOf(word[word.Length - 1]) + 1;
                }

                total += num;
            }
            Console.WriteLine($"{total:F2}");
        }
    }
}
