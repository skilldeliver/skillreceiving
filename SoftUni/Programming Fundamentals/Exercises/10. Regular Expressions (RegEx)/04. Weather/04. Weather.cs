using System;
using System.Text.RegularExpressions;
using System.Collections.Generic;
using System.Linq;

namespace _04._Weather
{
    class Program
    {
        static void Main(string[] args)
        {
            SortedDictionary<string, List<string>> data = new SortedDictionary<string, List<string>>();
            string regex = @"(?<city>[A-Z]{2})(?<temp>\d+\.\d+)(?<weather>[A-Za-z]+)";

            while (true)
            {
                string line = Console.ReadLine();
                if (line == "end") break;

                string[] tokens = line.Split('|');
                var matches = Regex.Matches(tokens[0], regex);

                if (tokens.Length > 1)
                {
                    foreach (Match match in matches)
                    {
                        var city = match.Groups["city"].Value;
                        var temp = match.Groups["temp"].Value;
                        var weather = match.Groups["weather"].Value;

                        if (data.ContainsKey(city))
                        {
                            data[city][0] = temp;
                            data[city][1] = weather;
                        }
                        else
                        {
                            data[city] = new List<string>();
                            data[city].Add(temp);
                            data[city].Add(weather);
                        }
                    }
                }

            }
            foreach (var entry in data.OrderBy(x => x.Value[0]).ToDictionary(x => x.Key, x => x.Value))
            {
                Console.WriteLine($"{entry.Key} => {double.Parse(entry.Value[0]):F2} => {entry.Value[1]}");
            }
        }
    }
}
