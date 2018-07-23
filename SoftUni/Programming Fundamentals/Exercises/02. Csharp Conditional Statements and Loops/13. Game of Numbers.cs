using System;

namespace _13._Game_of_Numbers
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            int m = int.Parse(Console.ReadLine());
            int mag = int.Parse(Console.ReadLine());

            int count = 0;
            for (int i = n; i <= m; i++)
            {
                for (int k = n; k <= m; k++)
                {
                    count += 1;
                    if (i + k == mag)
                    {
                        Console.WriteLine($"Number found! {k} + {i} = {mag}");
                        return;
                    }
                }
            }
            Console.WriteLine($"{count} combinations - neither equals {mag}");

        }
    }
}
