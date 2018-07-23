using System;

namespace _08._Sum_of_Odd_Numbers
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            int count = 0;
            int i = 0;
            int sum = 0;

            while (count <= n) {
                i++;
                if (i % 2 != 0)
                {
                    count += 1;
                    if (count <= n)
                    {
                        Console.WriteLine(i);
                        sum += i;
                    }
                }

            }
            Console.WriteLine("Sum: " + sum);
        }
    }
}