using System;
using System.Linq;
using System.Collections.Generic;


namespace _05._Hands_of_Cards
{
    class Program
    {
        static void Main(string[] args)
        {
            string line = Console.ReadLine();
            Dictionary<string, List<string>> hands = new Dictionary<string, List<string>>();
            List<string> power = new List<string>() { "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"};
            List<string> type = new List<string>() { "C", "D", "H", "S"};

            while (line != "JOKER"){
                string name = line.Split(':')[0];
                List<string> hand = line.Split(':')[1].Trim().Split(", ".ToCharArray(), StringSplitOptions.RemoveEmptyEntries).Distinct().ToList();

                if (hands.ContainsKey(name)) hands[name].AddRange(hand);
                else hands[name] = hand;
                line = Console.ReadLine();
            }

            DateTime dt = DateTime.Now;

            foreach (var entry in hands)
            {
                long sum = 0;
                foreach (string card in entry.Value.Distinct())
                {
                    long multiply = 0;
                    foreach (string t in type)
                    {
                        if (card.EndsWith(t))
                        {
                            multiply = type.IndexOf(t) + 1;
                            break;
                        }
                    }

                    long product = 0;
                    foreach (string p in power)
                    {
                        if (card.StartsWith(p))
                        {
                            product = (power.IndexOf(p) + 2) * multiply;
                            break;
                        }
                    }
                    sum += product;
                }
                Console.WriteLine(entry.Key + ": " + sum);

            }
            TimeSpan ts = DateTime.Now - dt;
            Console.WriteLine(ts.TotalSeconds.ToString());
        }
    }
}