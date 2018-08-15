using System;
using System.Linq;
using System.Collections.Generic;

namespace _04._Supermarket_Database
{
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<string, List<double>> data = new Dictionary<string, List<double>>();

            while (true)
            {
                string line = Console.ReadLine();
                if (line == "stocked") break;

                string[] info = line.Split(' ');

                if (data.ContainsKey(info[0]))
                {
                    data[info[0]][0] = double.Parse(info[1]);
                    data[info[0]][1] += double.Parse(info[2]);
                }
                else
                {
                    data[info[0]] = new List<double>();
                    data[info[0]].Add(double.Parse(info[1]));
                    data[info[0]].Add(double.Parse(info[2]));
                }
            }

            double grand = 0.0;
            foreach (var entry in data)
            {
                Console.WriteLine($"{entry.Key}: ${entry.Value[0]:F2} * {entry.Value[1]:F0} = ${entry.Value[0] * entry.Value[1]:F2}");
                grand += entry.Value[0] * entry.Value[1];
            }
            Console.WriteLine("------------------------------");
            Console.WriteLine($"Grand Total: ${grand:F2}");
        }
    }
}
