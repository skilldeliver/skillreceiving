using System;
using System.Collections.Generic;
using System.Linq;

namespace _06._User_Logs
{
    class Program
    {
        static void Main(string[] args)
        {
            string line = "";
            SortedDictionary<string, Dictionary<string, long>> data = new SortedDictionary<string, Dictionary<string, long>>();

            while (true)
            {
                line = Console.ReadLine();
                if (line == "end") break;

                string[] info = line.Split("= ".ToCharArray(), StringSplitOptions.RemoveEmptyEntries);

                try
                {
                    data[info[5]][info[1]] += 1;
                }
                catch (KeyNotFoundException)
                {
                    try
                    {
                        data.Add(info[5], new Dictionary<string, long>());
                    }
                    catch (ArgumentException){ }
                    
                    data[info[5]].Add(info[1], 1);
                }
                
            }

            foreach (var entry in data)
            {
                Console.WriteLine(entry.Key + ":");
                foreach (var item in entry.Value)
                {
                    Console.Write(item.Key + " => " + item.Value);

                    if (item.Key != entry.Value.Keys.Last()) Console.Write(", ");
                }
                Console.WriteLine(".");
            }
        }
    }
}
