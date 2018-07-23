using System;

namespace _07._Training_Hall_Equipment
{
    class Program
    {
        static void Main(string[] args)
        {
            double budget = double.Parse(Console.ReadLine());
            int numberItems = int.Parse(Console.ReadLine());
            double total = 0.0;

            for (int i = 1; i <= numberItems; i++)
            {
                string nameItem = Console.ReadLine();
                double priceItem = double.Parse(Console.ReadLine());
                int itemCount = int.Parse(Console.ReadLine());

                if (itemCount > 1)
                {
                    Console.WriteLine($"Adding {itemCount} {nameItem}s to cart.");
                }
                else
                {
                    Console.WriteLine($"Adding {itemCount} {nameItem} to cart.");
                }
                total += (priceItem * itemCount);
            }
            if (total <= budget)
            {
                Console.WriteLine($"Subtotal: ${total:f2}");
                Console.WriteLine($"Money left: ${budget - total:f2}");

            }
            else
            {
                Console.WriteLine($"Subtotal: ${total:f2}");
                Console.WriteLine($"Not enough. We need ${total - budget:f2} more.");
            }
        }
    }
}
