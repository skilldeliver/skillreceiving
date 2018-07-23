using System;

namespace _05._Character_Stats
{
    class Program
    {
        static void Main(string[] args)
        {
            string name = Console.ReadLine();
            int currHealth = int.Parse(Console.ReadLine());
            int maxHealth = int.Parse(Console.ReadLine());
            int currEnergy = int.Parse(Console.ReadLine());
            int maxEnergy = int.Parse(Console.ReadLine());

            int leftHealth = maxHealth - currHealth;
            int leftEnergy = maxEnergy - currEnergy;

            Console.WriteLine("Name: " + name);
            Console.WriteLine("Health: " + "|" + new string('|', currHealth) + new string('.', leftHealth) + "|");
            Console.WriteLine("Energy: " + "|" + new string('|', currEnergy) + new string('.', leftEnergy) + "|");
        }
    }
}
