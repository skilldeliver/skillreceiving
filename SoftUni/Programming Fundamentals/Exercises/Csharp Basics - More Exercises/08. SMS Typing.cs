using System;

namespace _08._SMS_Typing
{
    class Program
    {
        static void Main()
        {
            int n = int.Parse(Console.ReadLine());
            string[] week = new string[] { "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" };

            string result = "";
            for (int i = 1; i <= n; i++)
            {
                string input = Console.ReadLine();
                if (input != "0")
                {
                    int len = input.Length;
                    int mainDig = int.Parse(input[0].ToString());

                    int offset = (mainDig - 2) * 3;
                    if (mainDig == 8 || mainDig == 9)
                    {
                        offset += 1;
                    }

                    
                    result += week[offset + len - 1];
                }
                else result += " ";
            }
            Console.WriteLine(result);
        }
    }
}
