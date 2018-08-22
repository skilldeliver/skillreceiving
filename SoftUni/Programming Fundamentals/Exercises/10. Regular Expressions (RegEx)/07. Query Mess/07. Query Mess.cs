using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;
namespace _07._Query_Mess
{
    class Program
    {
        static void Main(string[] args)
        {
            string regex = @"([^&=?\s]*)(?=\=)=(?<=\=)([^&=\s]*)";
            string replace = @"((%20|\+)+)";
            string line = Console.ReadLine();

            while (!(line == "END"))
            {
                var matches = Regex.Matches(line, regex);
                Dictionary<string, List<string>> data = new Dictionary<string, List<string>>();

                foreach (Match match in matches)
                {
                    string label = Regex.Replace(match.Groups[1].Value, replace, w => " ").Trim();
                    string value = Regex.Replace(match.Groups[2].Value, replace, w => " ").Trim();

                    if (data.ContainsKey(label))
                    {
                        data[label].Add(value);
                    }
                    else
                    {
                        data[label] = new List<string>();
                        data[label].Add(value);
                    }
                }

                foreach (var entry in data)
                {
                    Console.Write($"{entry.Key}=[{string.Join(", ", entry.Value)}]");
                }
                Console.WriteLine();
                line = Console.ReadLine();
            }
        }
    }
}
