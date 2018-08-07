using System;

namespace _10._Sum_of_Chars
{
    class Program
    {
        static void Main(string[] args)
        {
            long n = long.Parse(Console.ReadLine());
            int sum = 0;

            for (int i = 0; i < n; i++)
            {
                char chr = Console.ReadLine()[0];
                sum += chr;
            }

            Console.WriteLine("The sum equals: " + sum);

        }
    }
}
