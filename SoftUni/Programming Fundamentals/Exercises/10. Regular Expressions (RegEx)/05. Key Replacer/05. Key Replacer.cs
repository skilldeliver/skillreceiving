using System;
using System.Text.RegularExpressions;
using System.Collections.Generic;
using System.Linq;

namespace _05._Key_Replacer
{
    class Program
    {
        static void Main(string[] args)
        {
            string line = Console.ReadLine();

            string regex = $@"^([a-zA-Z]+)[\\|\\<\\\\](.+)[\\|\\<\\\\]([a-zA-Z]+)$";
            var start = Regex.Match(line, regex).Groups[1].Value; 
            var end = Regex.Match(line, regex).Groups[3].Value;

            string input = Console.ReadLine();
            var matches = Regex.Matches(input, $@"{start}(?!{end})(.*?){end}");

            string final = "";

            foreach (Match match in matches)
            {
                final += match.Groups[1].Value;
            }

            if (final == "")
            {
                Console.WriteLine("Empty result");
            }
            else
            {
                Console.WriteLine(final);
            }
        }
    }
}
