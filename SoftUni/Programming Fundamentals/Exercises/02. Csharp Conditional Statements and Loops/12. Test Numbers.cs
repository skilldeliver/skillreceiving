using System;

namespace _12._Test_Numbers
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            int m = int.Parse(Console.ReadLine());
            int sum = int.Parse(Console.ReadLine());

            int total = 0;
            int count = 0;

            for (int i = n; i >= 1; i--)
            {
                for (int k = 1; k <= m; k++)
                {
                    total += (i * k) * 3;
                    count++;

                    if (total >= sum)
                    {
                        Console.WriteLine(count + " combinations");
                        Console.WriteLine($"Sum: {total} >= {sum}");
                        return;
                    }
                }
            }
            Console.WriteLine(count + " combinations");
            Console.WriteLine($"Sum: {total}");
        }
    }
}
