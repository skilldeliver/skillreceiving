using System;
using System.Linq;
using System.Text.RegularExpressions;

namespace _10._Regular_Expressions__RegEx____Exercises
{
    class Program
    {
        static void Main(string[] args)
        {
            string regex = @"(^|(?<=\s))(([a-zA-Z0-9]+)([\.\-_]?)([A-Za-z0-9]+)(@)([a-zA-Z]+([\.\-_][A-Za-z]+)+))(\b|(?=\s))";
            var matches = Regex.Matches(Console.ReadLine(), regex).Cast<Match>().Select(x => x.Value).ToList();

            Console.WriteLine(string.Join("\n", matches));
        }
    }
}
