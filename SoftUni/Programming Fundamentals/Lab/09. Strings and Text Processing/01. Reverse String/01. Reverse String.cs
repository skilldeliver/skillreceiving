using System;
using System.Linq;

namespace _09._Strings_and_Text_Processing___Lab
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(string.Join("", Console.ReadLine().ToCharArray().Reverse()));
        }
    }
}
