using System;

namespace _05._Only_Letters
{
    class Program
    {
        static void Main(string[] args)
        {
            string message = Console.ReadLine();
            string result = "";
            string last = "";
            string numbers = "1234567890";

            bool num = false;
            foreach (char let in message)
            {
                if (numbers.IndexOf(let) != -1)
                {
                    num = true;
                    last += let;
                }
                else
                {
                    result += let;
                    if (num) result += let;
                    last = "";
                    num = false;
                }
            }
            result += last;
            Console.WriteLine(result);
        }
    }
}
