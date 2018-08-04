using System;

namespace _13._Vowel_or_Digit
{
    class Program
    {
        static void Main(string[] args)
        {
            string n = Console.ReadLine();
            
            for (int i = 0; i <= 9; i++)
            {
                if (n == i.ToString())
                {
                    Console.WriteLine("digit");
                    return;
                }
            }

            if (n == "a" || n == "e" || n == "o" || n == "u" || n == "i" || n == "y")
            {
                Console.WriteLine("vowel");
            }
            else
            {
                Console.WriteLine("other");
            }
        }
    }
}
