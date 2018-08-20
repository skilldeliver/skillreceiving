using System;

namespace _03._Unicode_Characters
{
    class Program
    {
        static void Main(string[] args)
        {
            string line = Console.ReadLine();

            foreach (char c in line)
            {
                string num = ((int)c).ToString("x4");
                Console.Write("\\u" + num);
            }
        }
    }
}
