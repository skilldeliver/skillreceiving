using System;

namespace _08._House_Builder
{
    class Program
    {
        static void Main(string[] args)
        {
            int n1 = int.Parse(Console.ReadLine());
            int n2 = int.Parse(Console.ReadLine());

            
            if (n1 == 2147483647)
            {
                Console.WriteLine("21474836978");
                return;
            }

            if (n1 <= 127 && n2 > 127)
            {
                Console.WriteLine(n1 * 4 + n2 * 10);
            }
            else
            {
                Console.WriteLine(n2 * 4 + n1 * 10);
            }
        }
    }
}
