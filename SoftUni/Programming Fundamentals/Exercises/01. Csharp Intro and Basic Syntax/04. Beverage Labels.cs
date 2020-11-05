using System;

namespace _04._Beverage_Labels
{
    class Program
    {
        static void Main(string[] args)
        {
            string name = Console.ReadLine();
            int volume = int.Parse(Console.ReadLine());
            int energy = int.Parse(Console.ReadLine());
            int sugar = int.Parse(Console.ReadLine());

            double per = volume / 100.00;
            double energyy = energy * per;
            double sugary = sugar * per;

            Console.WriteLine(volume + "ml " + name + ":");
            Console.WriteLine(energyy + "kcal, " + sugary + "g sugars");
        }
    }
}
