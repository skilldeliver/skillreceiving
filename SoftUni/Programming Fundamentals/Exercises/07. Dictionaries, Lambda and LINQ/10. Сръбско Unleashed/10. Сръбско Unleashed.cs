using System;
using System.Linq;
using System.Collections.Generic;

namespace _10._Сръбско_Unleashed
{
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<string, Dictionary<string, int>> data = new Dictionary<string, Dictionary<string, int>>();

            while (true)
            {
                string line = Console.ReadLine();
                if (line == "End") break;
                if (!line.Contains(" @")) continue;
                string name = line.Substring(0, line.IndexOf(" @"));
                if (name.Split().Length > 3) continue;
                string[] splitLine = line.Substring(line.IndexOf("@") + 1).Split();
                if (splitLine.Length < 3) continue;
                string[] tickets = splitLine.Take(splitLine.Length - 2).ToArray();
                if (tickets.Length > 3) continue;
                string venue = String.Join(" ", tickets);
                int ticketPrice = 0;
                int ticketCount = 0;
                if (!int.TryParse(splitLine[splitLine.Length - 2], out ticketPrice)) continue;
                if (!int.TryParse(splitLine[splitLine.Length - 1], out ticketCount)) continue;
                int totalEarning = ticketCount * ticketPrice;

                if (!data.ContainsKey(venue)) data[venue] = new Dictionary<string, int>();
                if (data[venue].ContainsKey(name)) data[venue][name] += totalEarning;
                else data[venue][name] = totalEarning;
            }

            foreach (var item in data)
            {
                Console.WriteLine($"{item.Key}");
                foreach (var entry in item.Value.OrderBy(x => -x.Value))
                {
                    Console.WriteLine($"#  {entry.Key} -> {entry.Value}");
                }
            }
        }
    }
}