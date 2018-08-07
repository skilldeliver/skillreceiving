using System;

namespace _11._String_Concatenation
{
    class Program
    {
        static void Main(string[] args)
        {
            char chr = Console.ReadLine()[0];
            string which = Console.ReadLine();
            int n = int.Parse(Console.ReadLine());

            string result = "";

            for (int i = 1; i <= n; i++)
            {
                string word = Console.ReadLine();
                if (which == "odd")
                {
                    if (i % 2 != 0) result += word + chr;
                    
                }
                else
                {
                    if (i % 2 == 0) result += word + chr;
                }
            }
            
            Console.WriteLine(result.Remove(result.Length - 1));
        }
    }
}
