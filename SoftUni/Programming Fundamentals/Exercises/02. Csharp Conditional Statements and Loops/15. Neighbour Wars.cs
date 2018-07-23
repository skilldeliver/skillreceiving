using System;

namespace _15._Neighbour_Wars
{
    class Program
    {
        static void Main(string[] args)
        {
            int peshoDamage = int.Parse(Console.ReadLine());
            int goshoDamage = int.Parse(Console.ReadLine());

            int peshoHealth = 100;
            int goshoHealth = 100;

            int i = 0;
            while (peshoHealth > 0 || goshoHealth > 0)
            {
                i++;

                if (i % 2 != 0)
                {
                    goshoHealth -= peshoDamage;
                    if (goshoHealth <= 0) break;
                    Console.WriteLine("Pesho used Roundhouse kick and reduced Gosho to {0} health.", goshoHealth);
                }
                else
                {
                    peshoHealth -= goshoDamage;
                    if (peshoHealth <= 0) break;
                    Console.WriteLine("Gosho used Thunderous fist and reduced Pesho to {0} health.", peshoHealth);
                }
                if (i % 3 == 0)
                {
                    goshoHealth += 10;
                    peshoHealth += 10;
                }
            }

            if (peshoHealth > goshoHealth) Console.WriteLine($"Pesho won in {i}th round.");
            else Console.WriteLine($"Gosho won in {i}th round.");
        }
    }
}
