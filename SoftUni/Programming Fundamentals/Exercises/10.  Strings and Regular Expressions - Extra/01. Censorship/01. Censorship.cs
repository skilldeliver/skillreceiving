using System;

namespace _10.__Strings_and_Regular_Expressions___More2
{
    class Program
    {
        static void Main(string[] args)
        {
            string replace = Console.ReadLine();
            string line = Console.ReadLine();

            line = line.Replace(replace, new string('*', replace.Length));
            Console.WriteLine(line);
        }
    }
}
