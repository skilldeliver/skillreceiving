using System;
using System.Text.RegularExpressions;
using System.Linq;

namespace _06._Replace_a_Tag
{
    class Program
    {
        static void Main(string[] args)
        {
            string text = Console.ReadLine();

            while (text != "end")
            {
                string regex = @"<a.*?href.*?=(.*)>(.*?)<\/a>";
                string replacement = @"[URL href=$1]$2[/URL]";
                string replaced = Regex.Replace(text, regex, replacement);
                Console.WriteLine(replaced);

                text = Console.ReadLine();
            }
        }
    }
}
