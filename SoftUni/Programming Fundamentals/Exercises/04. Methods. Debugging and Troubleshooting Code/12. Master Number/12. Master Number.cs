using System;

namespace _12._Master_Number
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            MasterNumber(n);
            
        }

        static void MasterNumber(int n)
        {
            for (int i = 1; i <= n; i++)
            {
                if (IsPalindrome(i) && SumEvenlyDivBy7(i) && EvenDigit(i))
                {
                    Console.WriteLine(i);
                }
            }
        }

        static bool IsPalindrome(int num)
        {
            string strNum = num.ToString();
            string strNumR = "";

            for (int i = strNum.Length - 1; i >= 0; i--)
            {
                strNumR += strNum[i] + "";
            }

            return strNum == strNumR;
        }

        static bool SumEvenlyDivBy7(int num)
        {
            string strNum = num.ToString();
            int sum = 0;

            for (int i = strNum.Length - 1; i >= 0; i--)
            {
                sum += int.Parse(strNum[i] + "");
            }

            if (sum % 7 == 0) return true;
            return false;
        }

        static bool EvenDigit(int num)
        {
            string strNum = num.ToString();

            for (int i = strNum.Length - 1; i >= 0; i--)
            {
                if (int.Parse(strNum[i] + "") % 2 == 0) return true;
            }
            return false;
        }
    }
}
