using System;
using System.Linq;
using System.Collections.Generic;

namespace _07._Population_Counter
{
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<string, Dictionary<string, long>> data = new Dictionary<string, Dictionary<string, long>>();
            string line = "";

            while (true)
            {
                line = Console.ReadLine();
                if (line == "report") break;

                string[] info = line.Split('|');

                if (data.ContainsKey(info[1]))
                {
                    if (data[info[1]].ContainsKey("Total"))
                    {
                        data[info[1]]["Total"] += long.Parse(info[2]);
                    }
                    else
                    {
                        data[info[1]].Add("Total", long.Parse(info[2]));
                    }

                    if (data[info[1]].ContainsKey(info[0]))
                    {
                        data[info[1]][info[0]] += long.Parse(info[2]);
                    }
                    else
                    {
                        data[info[1]].Add(info[0], long.Parse(info[2]));
                    }
                }
                else

                {
                    data.Add(info[1], new Dictionary<string, long>());
                    if (data[info[1]].ContainsKey("Total"))
                    {
                        data[info[1]]["Total"] += long.Parse(info[2]);
                    }
                    else
                    {
                        data[info[1]].Add("Total", long.Parse(info[2]));
                    }

                    if (data[info[1]].ContainsKey(info[0]))
                    {
                        data[info[1]][info[0]] += long.Parse(info[2]);
                    }
                    else
                    {
                        data[info[1]].Add(info[0], long.Parse(info[2]));
                    }
                }
            }

            foreach (var entry in data.OrderByDescending(x => x.Value["Total"]).ToDictionary(x => x.Key, x => x.Value))
            {
                Console.WriteLine($"{entry.Key} (total population: {data[entry.Key]["Total"]})");

                foreach (var item in entry.Value.OrderByDescending(y => y.Value))
                {
                    if (item.Key != "Total") Console.WriteLine("=>" + item.Key + ": " + item.Value);
                }
            }


        }
    }
}
