using System;

namespace _04._Tourist_Information
{
    class Program
    {
        static void Main(string[] args)
        {
            string unit = Console.ReadLine();
            double value = double.Parse(Console.ReadLine());

            switch (unit)
            {
                case "miles":
                    Console.WriteLine($"{value} {unit} = {value * 1.6:F2} kilometers");
                    break;
                case "inches":
                    Console.WriteLine($"{value} {unit} = {value * 2.54:F2} centimeters");
                    break;
                case "feet":
                    Console.WriteLine($"{value} {unit} = {value * 30:F2} centimeters");
                    break;
                case "yards":
                    Console.WriteLine($"{value} {unit} = {value * 0.91:F2} meters");
                    break;
                case "gallons":
                    Console.WriteLine($"{value} {unit} = {value * 3.8:F2} liters");
                    break;
            }
        }
    }
}
