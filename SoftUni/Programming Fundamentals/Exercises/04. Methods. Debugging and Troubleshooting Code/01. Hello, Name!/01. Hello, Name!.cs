using System;

namespace Methods._Debugging_and_Troubleshooting___Exercises
{
    class Program
    {
        static void Main(string[] args)
        {
            string name = Console.ReadLine();
            PrintName(name);
        }

        static void PrintName(string name)
        {
            Console.WriteLine("Hello, " + name + "!");
        }
    }
}
