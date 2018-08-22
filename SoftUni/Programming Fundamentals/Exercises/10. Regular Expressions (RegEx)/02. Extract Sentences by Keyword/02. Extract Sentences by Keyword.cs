using System;
using System.Linq;
using System.Text.RegularExpressions;

namespace _02._Extract_Sentences_by_Keyword
{
    class Program
    {
        static void Main(string[] args)
        {
            string word = Console.ReadLine();
            string regex = $@"\b{word}\b";
            string[] text = Console.ReadLine().Split(".!?".ToCharArray(), StringSplitOptions.RemoveEmptyEntries);

            foreach (string line in text)
            {
                if (Regex.IsMatch(line, regex))
                {
                    if (line.StartsWith(" "))
                    {
                        string nline = line.Remove(0, 1);
                        Console.WriteLine(nline);
                    }
                    else
                    {
                        Console.WriteLine(line);
                    }
                    
                }
            }

            foreach (var item in collection)
            {

            }
        }
    }
}
