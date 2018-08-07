using System;

namespace _08._Center_Point
{
    class Program
    {
        static void Main(string[] args)
        {
            double x1 = double.Parse(Console.ReadLine());
            double y1 = double.Parse(Console.ReadLine());
            double x2 = double.Parse(Console.ReadLine());
            double y2 = double.Parse(Console.ReadLine());

            Console.WriteLine(CenterPoint(x1, y1, x2, y2));
        }

        static string CenterPoint(double x1, double y1, double x2, double y2)
        {
            double sum1 = Math.Abs(x1) + Math.Abs(y1);
            double sum2 = Math.Abs(x2) + Math.Abs(y2);

            if (sum1 <= sum2) return "(" + x1 + ", " + y1 + ")";
            return "(" + x2 + ", " + y2 + ")";
        }
    }
}
