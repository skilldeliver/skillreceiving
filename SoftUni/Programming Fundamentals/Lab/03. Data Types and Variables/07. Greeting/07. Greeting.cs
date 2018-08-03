using System;

namespace _07._Greeting
{
    class Program
    {
        static void Main(string[] args)
        {
            string firstName = Console.ReadLine();
            string lastName = Console.ReadLine();
            int years = int.Parse(Console.ReadLine());

            Console.WriteLine($"Hello, {firstName} {lastName}.\r\nYou are {years} years old.");
        }
    }
}
