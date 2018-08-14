using System;
using System.Linq;
using System.Collections.Generic;

namespace _11._Dragon_Army
{
    class Program
    {
        static void Main(string[] args)
        {

            int n = int.Parse(Console.ReadLine());
            Dictionary<string, SortedDictionary<string, Dictionary<string, long>>> data = new Dictionary<string, SortedDictionary<string, Dictionary<string, long>>>();

            for (int i = 0; i < n; i++)
            {
                string[] info = Console.ReadLine().Split();
                string type = info[0];
                string name = info[1];
                string damage = info[2];
                string health = info[3];
                string armor = info[4];

                if (data.ContainsKey(type))
                {
                    if (data[type].ContainsKey(name)) data = Parse(data, type, name, damage, health, armor);
                    else {
                        data[type][name] = new Dictionary<string, long>();
                        data = Parse(data, type, name, damage, health, armor);
                    }
                }
                else {
                    data[type] = new SortedDictionary<string, Dictionary<string, long>>();
                    data[type][name] = new Dictionary<string, long>();
                    data = Parse(data, type, name, damage, health, armor);
                }
            }
            Print(data);

        }

        static void Print(Dictionary<string, SortedDictionary<string, Dictionary<string, long>>> data)
        {
            foreach (var entry in data)
            {
                Console.Write(entry.Key + "::(");
                long damage = 0;
                long health = 0;
                long armor = 0;
                foreach (var item in entry.Value)
                {
                    foreach (var element in item.Value)
                    {
                        if (element.Key == "damage") damage += element.Value;
                        else if (element.Key == "health") health += element.Value;
                        else if (element.Key == "armor") armor += element.Value;
                    }
                }
                Console.Write($"{damage / (double)entry.Value.Count:F2}/");
                Console.Write($"{health / (double)entry.Value.Count:F2}/");
                Console.WriteLine($"{armor / (double)entry.Value.Count:F2})");

                foreach (var item in entry.Value)
                {
                    Console.WriteLine($"-{item.Key} -> damage: {item.Value["damage"]}, health: {item.Value["health"]}, armor: {item.Value["armor"]}");
                }
            }
        }

        static Dictionary<string, SortedDictionary<string, Dictionary<string, long>>> Parse(Dictionary<string, SortedDictionary<string, Dictionary<string, long>>> data, string type, string name, string damage, string health, string armor)
        {
            data[type][name]["damage"] = Damage(damage);
            data[type][name]["health"] = Health(health);
            data[type][name]["armor"] = Armor(armor);

            return data;
        }

        static long Damage(string str)
        {
            if (str == "null") return 45;
            return long.Parse(str);
        }
        static long Health(string str)
        {
            if (str == "null") return 250;
            return long.Parse(str);
        }
        static long Armor(string str)
        {
            if (str == "null") return 10;
            return long.Parse(str);
        }
    }
}
