using System;

namespace _02._Max_Method
{
    class Program
    {
        static void Main(string[] args)
        {
            int a = int.Parse(Console.ReadLine());
            int b = int.Parse(Console.ReadLine());
            int c = int.Parse(Console.ReadLine());

            Console.WriteLine(GetMax(c, GetMax(a, b)));
        }

        static int GetMax(int a, int b)
        {
            if (a > b) return a;
            return b;
        }
    }
}
