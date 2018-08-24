using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace _03._Word_Count
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] words = File.ReadAllLines(@"words.txt")[0].ToLower().Split();
            Dictionary<string, int> data = new Dictionary<string, int>();
            string[] lines = File.ReadAllLines(@"text.txt");

            for (int i = 0; i < lines.Length; i++)
            {
                string[] Allwords = lines[i].Split(",.!- ".ToCharArray(), StringSplitOptions.RemoveEmptyEntries);
                
                foreach (string w in Allwords)
                {
                    string word = w.ToLower();
                    if (words.Contains(word))
                    {
                        if (data.ContainsKey(word))
                        {
                            data[word] += 1;
                        }
                        else
                        {
                            data[word] = 1;
                        }
                    }
                }
            }

            List<string> newWords = new List<string>();

            foreach (var entry in data.OrderByDescending(x => x.Value))
            {
                newWords.Add($"{entry.Key} - {entry.Value}");
            }
            File.WriteAllLines(@"output.txt", newWords);
            Console.WriteLine("Done!");
        }
    }
}
