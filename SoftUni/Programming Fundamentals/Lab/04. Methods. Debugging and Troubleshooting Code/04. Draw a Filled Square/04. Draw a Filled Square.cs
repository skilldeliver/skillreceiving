using System;

namespace _04._Draw_a_Filled_Square
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());

            PrintHeaderFooter(n);
            for (int i = 0; i < n - 2; i++)
            {
                PrintMiddle(n);
            }
            PrintHeaderFooter(n);
        }

        static void PrintHeaderFooter(int n)
        {
            Console.WriteLine(new string('-', 2 * n));
        }

        static void PrintMiddle(int n)
        {
            Console.Write("-");

            for (int i = 1; i < n; i++)
            {
                Console.Write("\\/");
            }
            Console.WriteLine("-");
        }
    }
}
