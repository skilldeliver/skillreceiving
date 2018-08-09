using System;

namespace _05._Pizza_Ingredients
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] ingredients = Console.ReadLine().Split(' ');
            long len = long.Parse(Console.ReadLine());
            string[] usedIngredients = new string[10];

            long count = -1;

            foreach (string item in ingredients)
            {
                if (item.Length == len && count < 9)
                {
                    Console.WriteLine("Adding " + item + ".");
                    count += 1;
                    usedIngredients[count] = item;
                }
            }

            Console.WriteLine($"Made pizza with total of {count + 1} ingredients.");
            Console.Write("The ingredients are: ");
            for (int i = 0; i <= count; i++)
            {
                Console.Write(usedIngredients[i]);
                if (i != count)
                {
                    Console.Write(", ");
                }
                else
                {
                    Console.Write(".");
                }
                
            }


        }
    }
}
