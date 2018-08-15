using System;
using System.Linq;
using System.Collections.Generic;

namespace _03._Immune_System
{
    class Program
    {
        static void Main(string[] args)
        {
            List<string> viruses = new List<string>();
            long immuneHealth = long.Parse(Console.ReadLine());
            long constHealth = immuneHealth;

            while (true)
            {
                string line = Console.ReadLine();
                if (line == "end") break;

                long timeDefeat = 0;
                long virusStrenght = VirusStrenght(line);
                Console.Write("Virus " + line + ": " + virusStrenght);

                if (viruses.Contains(line))
                {
                    timeDefeat = (virusStrenght * line.Length) / 3;
                }
                else
                {
                    timeDefeat = virusStrenght * line.Length;
                }

                Console.WriteLine(" => " + timeDefeat + " seconds");
                viruses.Add(line);
                
                if (immuneHealth >= timeDefeat)
                {
                    Console.WriteLine(line + " defeated in " + TimeFormat(timeDefeat));
                }
                else
                {
                    Console.WriteLine("Immune System Defeated.");
                    return;
                }

                immuneHealth -= timeDefeat;
                Console.WriteLine("Remaining health: " + immuneHealth);

                immuneHealth = (long)(immuneHealth * 1.2);
                if (immuneHealth > constHealth) immuneHealth = constHealth;
            }
            Console.WriteLine("Final Health: " + immuneHealth);
        }

        static string TimeFormat(long time)
        {
            long mins = time % 60;
            long hours = (time - mins) / 60;

            return hours + "m " + mins + "s.";
        }

        static long VirusStrenght(string virus)
        {
            long tot = 0;
            foreach(char chr in virus)
            {
                tot += chr;
            }

            return tot / 3;
        }
    }
}
