using System;
using System.Text.RegularExpressions;

namespace _10._Regular_Expressions__RegEx____Lab
{
    class Program
    {
        static void Main(string[] args)
        {
            string regex = @"\b[A-Z][a-z]+ [A-Z][a-z]+\b";

            string names = Console.ReadLine();
            MatchCollection matches = Regex.Matches(names, regex);

            foreach (Match name in matches)
            {
                Console.Write(name.Value + " ");
            }
            Console.WriteLine();
        }
    }
}
