using System;

namespace _14._Magic_Letter
{
    class Program
    {
        static void Main(string[] args)
        {
            char a = Console.ReadLine()[0];
            char b = Console.ReadLine()[0];
            char c = Console.ReadLine()[0];

            for (int i = a; i <= b; i++)
            {
                for (int j = a; j <= b; j++)
                {
                    for (int k = a; k <= b; k++)
                    {
                        if (i != c && j != c && k != c)
                        {
                            Console.Write("{0}{1}{2} ", (char)i, (char)j, (char)k);
                        }
                    }
                }

            }
        }
    }
}
