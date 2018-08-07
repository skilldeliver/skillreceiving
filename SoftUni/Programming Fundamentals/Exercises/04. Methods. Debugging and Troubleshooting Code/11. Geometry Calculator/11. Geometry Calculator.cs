using System;

namespace _11._Geometry_Calculator
{
    class Program
    {
        static void Main(string[] args)
        {
            string figure = Console.ReadLine();

            if (figure == "square" || figure == "circle")
            {
                double a = double.Parse(Console.ReadLine());
                Console.WriteLine("{0:F2}", GeometryArea(figure, a));
            }
            else
            {
                double a = double.Parse(Console.ReadLine());
                double b = double.Parse(Console.ReadLine());
                Console.WriteLine("{0:F2}", GeometryArea(figure, a, b));
            }

        }

        static double GeometryArea(string figure, double a, double b = 0.0)
        {
            double area = 0.0;

            if (figure == "triangle")
            {
                area = (a * b) / 2.0;
            }
            else if (figure == "square")
            {
                area = a * a;
            }
            else if (figure == "rectangle")
            {
                area = a * b;
            }
            else if (figure == "circle")
            {
                area = Math.PI * a * a;
            }

            return area;
        }
    }
}
