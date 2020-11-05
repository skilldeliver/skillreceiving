using System;

namespace Csharp_Basics___More_Exercises
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());

            int space = -1;
            int spaceBetween = n;

            for (int i = 1; i <= (n - 1) / 2; i++)
            {
                space++;
                spaceBetween -= 2;
                Console.WriteLine(new string(' ', space) + "x" + new string(' ', spaceBetween) + "x");
            }
            Console.WriteLine(new string(' ', (n - 1) / 2) + "x");

            spaceBetween = -1;
            space = (n - 1) / 2;

            for (int i = 1; i <= (n - 1) / 2; i++)
            {
                space--;
                spaceBetween += 2;
                Console.WriteLine(new string(' ', space) + "x" + new string(' ', spaceBetween) + "x");
            }

        }
    }
}
