using System;

namespace _03._Water_Overflow
{
    class Program
    {
        static void Main(string[] args)
        {
            int all = 0;
            int n = int.Parse(Console.ReadLine());

            for (int i = 0; i < n; i++)
            {
                int liters = int.Parse(Console.ReadLine());

                if (liters + all > 255)
                {
                    Console.WriteLine("Insufficient capacity!");
                }
                else
                {
                    all += liters;
                }
            }
            Console.WriteLine(all);
        }
    }
}
