using System;
using System.Text;
using System.Linq;
using System.Text.RegularExpressions;

namespace _08._Use_Your_Chains__Buddy
{
    class Program
    {
        static void Main(string[] args)
        {
            string line = Console.ReadLine();
            string pattern = @"(?<=<p>).*?(?=<\/p>)";
            var regex = new Regex(pattern);
            string result = "";

            foreach (Match match in regex.Matches(line))
            {
                var newString = Regex.Replace(match.Value, "[^a-z0-9]", " ");

                foreach (char chr in newString)
                {
                    if (char.IsLower(chr))
                    {
                        if (chr < 110)
                        {
                            result += (char)(chr + 13);
                        }
                        else if (chr >= 110)
                        {
                            result += (char)(chr - 13);
                        }
                    }
                    else
                    {
                        result += chr;
                    }
                }
            }
            Console.WriteLine(Regex.Replace(result, @"\s+", " "));
        }
    }
}
