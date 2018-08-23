using System;
using System.Linq;
using System.Collections.Generic;
using System.Text.RegularExpressions;

namespace _06._Email_Statistics
{
    class Program
    {
        static void Main(string[] args)
        {
            //distinct the names
            string regex = @"^(?<name>[a-zA-Z]{5,})@(?<email>[a-z]{3,}(\.com|\.bg|\.org))$";
            int n = int.Parse(Console.ReadLine());
            Dictionary<string, List<string>> data = new Dictionary<string, List<string>>();

            for (int i = 0; i < n; i++)
            {
                string user = Console.ReadLine();
                if (Regex.IsMatch(user, regex))
                {
                    string name = Regex.Match(user, regex).Groups["name"].Value;
                    string email = Regex.Match(user, regex).Groups["email"].Value;

                    if (data.ContainsKey(email))
                    {
                        data[email].Add(name);
                    }
                    else
                    {
                        data[email] = new List<string>();
                        data[email].Add(name);
                    }
                }
            }

            foreach (var entry in data.OrderByDescending(x => x.Value.Count))
            {
                Console.WriteLine(entry.Key + ":");
                foreach (string name in entry.Value.Distinct())
                {
                    Console.WriteLine("### " + name);
                }
            }
        }
    }
}
