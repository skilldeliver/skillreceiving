using System;

namespace _02._Count_Substring_Occurrences
{
    class Program
    {
        static void Main(string[] args)
        {
            string input = Console.ReadLine().ToLower();
            string search = Console.ReadLine().ToLower();

            int i = 0;
            int index = input.IndexOf(search);

            while (index != -1)
            {
                i++;
                index = input.IndexOf(search, index + 1);
            }
            Console.WriteLine(i);
        }
    }
}
