using System;
using System.Linq;

namespace _06._Reverse_Array_of_Strings
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] array = Console.ReadLine().Split(' ').ToArray();
            
            foreach(var item in array.Reverse())
            {
                Console.WriteLine(item + " ");
            }
        }
    }
}
