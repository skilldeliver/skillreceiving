using System;
using System.Text.RegularExpressions;

namespace _08._Mines
{
    class Program
    {
        static void Main(string[] args)
        {
            string line = Console.ReadLine();
            string regex = @"<.{2}>";
            var matches = Regex.Matches(line, regex);
            int lenght = line.Length;

            foreach (Match match in matches)
            {
                int replace = Math.Abs(match.Value[1] - match.Value[2]);
                Regex regex2 = new Regex($@".{{0,{replace}}}{match.Value}.{{0,{replace}}}");
                Match match2 = regex2.Match(line, 1);
                line = regex2.Replace(line, new string('_', match2.Value.Length));
            }

            if (line.Length != lenght) line = "_" + line;
            Console.WriteLine(line);
        }
    }
}
