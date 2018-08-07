using System;

namespace _04._Numbers_in_Reversed_Order
{
    class Program
    {
        static void Main(string[] args)
        {
            decimal num = decimal.Parse(Console.ReadLine());
            Console.WriteLine(ReverseNumber(num));
        }

        static string ReverseNumber(decimal num)
        {
            string strNum = num.ToString();
            string result = "";

            for (int i = strNum.Length - 1; i >= 0; i--)
            {
                result += strNum[i] + "";
            }

            return result;
        }
    }
}
