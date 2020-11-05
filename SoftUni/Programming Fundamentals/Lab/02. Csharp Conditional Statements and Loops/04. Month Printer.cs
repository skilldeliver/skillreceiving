using System;

namespace _04._Month_Printer
{
    class Program
    {
        static void Main(string[] args)
        {
            int month = int.Parse(Console.ReadLine());
            
            switch (month)
            {
                case 1:
                    Console.WriteLine("January");
                    break;
                case 2:
                    Console.WriteLine("February");
                    break;
                case 3:
                    Console.WriteLine("March");
                    break;
            }
        }
    }
}
