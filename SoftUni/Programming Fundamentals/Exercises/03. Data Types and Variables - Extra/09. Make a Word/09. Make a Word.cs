using System;

namespace _09._Make_a_Word
{
    class Program
    {
        static void Main(string[] args)
        {
            long n = long.Parse(Console.ReadLine());
            string word = "";

            for (int i = 0; i < n; i++)
            {
                char chr = Console.ReadLine()[0];
                word += chr;
            }

            Console.WriteLine("The word is: " + word);
        }
    }
}
