using System;

namespace _03._Text_Filter
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] bannedWords = Console.ReadLine().Split(',');
            string text = Console.ReadLine();

            string newText = "";
            foreach (string banned in bannedWords)
            {
                text = text.Replace(banned.Trim(), new string('*', banned.Trim().Length));
            }
            Console.WriteLine(text);
        }
    }
}
