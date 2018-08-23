using System;

namespace _04._Morse_Code_Upgraded
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] letters = Console.ReadLine().Split('|');

            string result = "";
            foreach (string num in letters)
            {
                result += Decipher(num);
            }

            Console.WriteLine(result);
        }

        static char Decipher(string num)
        {
            int totalSum = 0;

            foreach (char i in num)
            {
                if (i == '0') totalSum += 3;
                else totalSum += 5;
            }
            
            int add = 1;

            num += 'j';
            for (int i = 1; i < num.Length; i++)
            {
                if (num[i] == num[i - 1])
                {
                    add += 1;
                }
                else if(add != 1) 
                {
                    totalSum += add;
                    add = 1;
                }
            }

            return (char)totalSum;
        }
    }
}
