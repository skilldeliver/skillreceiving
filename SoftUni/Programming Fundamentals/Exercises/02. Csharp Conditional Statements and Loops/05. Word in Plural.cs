using System;

namespace _05._Word_in_Plural
{
    class Program
    {
        static void Main(string[] args)
        {
            string word = Console.ReadLine();

            int num = word.Length;
            if (word.EndsWith("y"))
            {
                word = word.Remove(num - 1);
                Console.WriteLine(word + "ies");

            }
            else if (word.EndsWith("o") || word.EndsWith("ch") || word.EndsWith("s") || word.EndsWith("sh") || word.EndsWith("x") || word.EndsWith("z"))
            {
                Console.WriteLine(word + "es");
            }
            else
            {
                Console.WriteLine(word + "s");
            }


        }
    }
}
