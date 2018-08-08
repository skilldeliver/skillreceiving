using System;

namespace _05._Arrays___Exercises
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] text1 = Console.ReadLine().Split(' ');
            string[] text2 = Console.ReadLine().Split(' ');
            string[] arr1 = { };
            string[] arr2 = { };

            if (text1.Length >= text2.Length)
            {
                arr1 = text1;
                arr2 = text2;
            }
            else
            {
                arr1 = text2;
                arr2 = text1;
            }

            int n1 = arr1.Length;
            int n2 = arr2.Length;
            int count = 0;
            bool toCount = true;

            for (int i = 0; i < n2; i++)
            {
                if (toCount && arr1[i] == arr2[i])
                {
                    count += 1;
                }
                else
                {
                    toCount = false;
                }
            }

            toCount = true;
            int countR= 0;
            int j = n1;

            for (int i = n2 - 1; i >= 0; i--)
            {
                j -= 1;
                if (toCount && arr1[j] == arr2[i])
                {
                    countR += 1;
                }
                else
                {
                    toCount = false;
                }
            }

            if (count >= countR) Console.WriteLine(count);
            else Console.WriteLine(countR);
            
        }
    }
}
