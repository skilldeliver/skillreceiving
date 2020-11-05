using System;

namespace _07._Cake_Ingredients
{
    class Program
    {
        static void Main(string[] args)
        {
            int count = 0;
            for (int i = 1; i <= 20; i++)
            {
                
                string ingredient = Console.ReadLine();

                if (ingredient == "Bake!")
                {
                    break;
                }
                Console.WriteLine("Adding ingredient " + ingredient + ".");
                count++;
            }
            Console.WriteLine($"Preparing cake with {count} ingredients.");
        }
    }
}
