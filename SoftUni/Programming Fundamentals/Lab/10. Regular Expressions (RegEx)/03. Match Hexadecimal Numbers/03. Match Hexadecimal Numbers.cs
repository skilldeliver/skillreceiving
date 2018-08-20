using System;
using System.Linq;
using System.Text.RegularExpressions;

namespace _03._Match_Hexadecimal_Numbers
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(string.Join(" ", Regex.Matches(Console.ReadLine(), @"\b(?:0x)?[0-9A-F]+\b").Cast<Match>().Select(a => a.Value).ToArray()));
        }
    }
}
