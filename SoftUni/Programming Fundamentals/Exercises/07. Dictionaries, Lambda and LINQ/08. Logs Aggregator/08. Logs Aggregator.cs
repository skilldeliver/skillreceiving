using System;
using System.Linq;
using System.Collections.Generic;

namespace _08._Logs_Aggregator
{
    class Program
    {
        static void Main(string[] args)
        {
            SortedDictionary<string,  SortedDictionary<string, long>> data = new SortedDictionary<string, SortedDictionary<string, long>>();
            int n = int.Parse(Console.ReadLine());

            for (int i = 0; i < n; i++)
            {
                string[] line = Console.ReadLine().Split(' ');

                if (data.ContainsKey(line[1]))
                {
                    if (data[line[1]].ContainsKey(line[0]))
                    {
                        data[line[1]][line[0]] += long.Parse(line[2]);
                    }
                    else
                    {
                        data[line[1]][line[0]] = long.Parse(line[2]);
                    }
                }
                else
                {
                    data.Add(line[1], new SortedDictionary<string, long>());
                    data[line[1]].Add(line[0], long.Parse(line[2]));
                }
            }

            foreach (var entry in data)
            {
                Console.Write(entry.Key + ": ");
                long sum = 0;
                List<string> list = new List<string>();
                foreach (var item in entry.Value)
                {
                    sum += item.Value;
                    list.Add(item.Key);
                }
                Console.Write(sum + " [");
                Console.Write(string.Join(", ", list));
                Console.WriteLine("]");
            }
            
        }
    }
}
