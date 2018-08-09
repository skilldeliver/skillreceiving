using System;
using System.Linq;

namespace _07._Inventory_Matcher
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] products = Console.ReadLine().Split(' ');
            long[] quanity = Console.ReadLine().Split(' ').Select(long.Parse).ToArray();
            decimal[] price = Console.ReadLine().Split(' ').Select(decimal.Parse).ToArray();

            string line = "";
            while (line != "done")
            {
                line = Console.ReadLine();

                long index = Array.IndexOf(products, line);

                if (index >= 0)
                {
                    Console.WriteLine($"{products[index]} costs: {price[index]}; Available quantity: {quanity[index]}");
                }
            }
        }
    }
}
