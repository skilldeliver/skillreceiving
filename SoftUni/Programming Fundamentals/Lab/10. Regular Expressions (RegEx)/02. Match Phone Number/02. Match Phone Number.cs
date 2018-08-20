using System;
using System.Linq;
using System.Text.RegularExpressions;

namespace _02._Match_Phone_Number
{
    class Program
    {
        static void Main(string[] args)
        {
            string regex = @"(\+359([ -])2(\2)(\d{3})(\2)(\d{4}))\b";
            string phones = Console.ReadLine();
            var matches = Regex.Matches(phones, regex).Cast<Match>().Select(a => a.Value.Trim()).ToArray();

            Console.WriteLine(string.Join(", ", matches));

        }
    }
}
