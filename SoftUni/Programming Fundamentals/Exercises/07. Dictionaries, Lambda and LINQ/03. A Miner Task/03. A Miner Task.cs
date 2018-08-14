using System;
using System.Collections.Generic;

namespace _03._A_Miner_Task
{
    class Program
    {
        static void Main(string[] args)
        {
            string resource = "";
            long quanity = 0;

            Dictionary<string, long> dict = new Dictionary<string, long>();

            while (true)
            {
                resource = Console.ReadLine();
                if (resource == "stop") break;
                quanity = long.Parse(Console.ReadLine());

                if (dict.ContainsKey(resource))
                {
                    dict[resource] += quanity;
                }
                else
                {
                    dict[resource] = quanity;
                }

            }

            foreach (var entry in dict)
            {
                Console.WriteLine(entry.Key + " -> " + entry.Value);
            }
        }
    }
}
