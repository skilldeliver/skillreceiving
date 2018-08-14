using System;
using System.Linq;
using System.Collections.Generic;

namespace _09._Legendary_Farming
{
    class Program
    {
        static void Main(string[] args)
        {
            SortedDictionary<string, long> special = new SortedDictionary<string, long>();
            special.Add("shards", 0);
            special.Add("fragments", 0);
            special.Add("motes", 0);
            SortedDictionary<string, long> junk = new SortedDictionary<string, long>();
            string legendary = "";
            bool loop = true;


             while (loop)
             {

                string[] materials = Console.ReadLine().ToLower().Split(' ');
                for (int i = 0; i < materials.Length; i += 2)
                {
                    if (special.ContainsKey(materials[i + 1]))
                    {
                        special[materials[i + 1]] += long.Parse(materials[i]);

                        if (special[materials[i + 1]] >= 250)
                        {
                            special[materials[i + 1]] -= 250;
                            if (materials[i + 1] == "shards") legendary = "Shadowmourne obtained!";
                            else if (materials[i + 1] == "fragments") legendary = "Valanyr obtained!";
                            else legendary = "Dragonwrath obtained!";

                            loop = false;
                            break;
                        }
                    }
                    else
                    {
                        if (junk.ContainsKey(materials[i + 1]))
                        {
                            junk[materials[i + 1]] += long.Parse(materials[i]);
                        }
                        else
                        {
                            junk.Add(materials[i + 1], long.Parse(materials[i]));
                        }
                    }
                }

            }
            

            Console.WriteLine(legendary);
            foreach (var entry in special.OrderByDescending(x => x.Value))
            {
                Console.WriteLine(entry.Key + ": " + entry.Value);
            }

            foreach (var entry in junk)
            {
                Console.WriteLine(entry.Key + ": " + entry.Value);
            }
        }
    }
}
