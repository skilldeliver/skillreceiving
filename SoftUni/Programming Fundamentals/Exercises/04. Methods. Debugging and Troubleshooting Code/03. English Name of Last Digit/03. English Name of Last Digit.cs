using System;

namespace _03._English_Name_of_Last_Digit
{
    class Program
    {
        static void Main(string[] args)
        {
            decimal num = decimal.Parse(Console.ReadLine());
            Console.WriteLine(EngNameOfLastDig(num));
        }

        static string EngNameOfLastDig(decimal num)
        {
            ulong number = (ulong)Math.Abs(Math.Round(num));
            ulong lastDigit = number % 10;

            string word = "";
            if (lastDigit == 0) word = "zero";
            else if (lastDigit == 1) word = "one";
            else if (lastDigit == 2) word = "two";
            else if (lastDigit == 3) word = "three";
            else if (lastDigit == 4) word = "four";
            else if (lastDigit == 5) word = "five";
            else if (lastDigit == 6) word = "six";
            else if (lastDigit == 7) word = "seven";
            else if (lastDigit == 8) word = "eight";
            else if (lastDigit == 9) word = "nine";
            return word;
        }
    }
}
