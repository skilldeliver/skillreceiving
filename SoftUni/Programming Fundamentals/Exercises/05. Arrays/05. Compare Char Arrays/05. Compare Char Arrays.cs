using System;
using System.Linq;
using System.Collections;

namespace _05._Compare_Char_Arrays
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] text1 = Console.ReadLine().Split(' ');
            string[] text2 = Console.ReadLine().Split(' ');
            char[] arr1 = StringArrToCharArr(text1);
            char[] arr2 = StringArrToCharArr(text2);

            for (int i = 0; i < MinLenght(arr1, arr2); i++)
            {
                if ((int)arr1[i] < (int)arr2[i])
                {
                    PrintArrays(arr1, arr2);
                    return;
                }
                else if ((int)arr2[i] < (int)arr1[i])
                {
                    PrintArrays(arr2, arr1);
                    return;
                }
            }

            if (arr1.Length <= arr2.Length)
            {
                PrintArrays(arr1, arr2);
            }
            else
            {
                PrintArrays(arr2, arr1);
            }

        }

        static void PrintArrays(char[] firstPrint, char[] secondPrint)
        {
            foreach (char item in firstPrint)
            {
                Console.Write(item + "");
            }
            Console.WriteLine();

            foreach (char item in secondPrint)
            {
                Console.Write(item + "");
            }
        }

        static int MinLenght(char[] arr1, char[] arr2) 
        {
            if (arr1.Length <= arr2.Length)
            {
                return arr1.Length;
            }

            return arr2.Length;
        }

        static char[] StringArrToCharArr(string[] arr)
        {
            char[] newArr = new char[arr.Length];

            for (int i = 0; i < arr.Length; i++)
            {
                newArr[i] = arr[i][0];
            }

            return newArr;
        }
    }
}
