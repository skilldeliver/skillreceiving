using System;
using System.Linq;
using System.Text.RegularExpressions;

namespace _05._Match_Numbers
{
    class Program
    {
        static void Main(string[] args)
        {
            string regex = @"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))";
            string numString = Console.ReadLine();
            var numbers = Regex.Matches(numString, regex).Cast<Match>().Select(a => a.Value.Trim()).ToArray();
            Console.WriteLine(string.Join(" ", numbers));

        }
    }
}
