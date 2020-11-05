using System;

namespace _02._Rectangle_Area
{
    class Program
    {
        static void Main(string[] args)
        {
            double width = double.Parse(Console.ReadLine());
            double height = double.Parse(Console.ReadLine());

            double area = width * height;
            Console.WriteLine($"{area:f2}");

        }
    }
}
