using System;

namespace _03._Megapixels
{
    class Program
    {
        static void Main(string[] args)
        {
            int width = int.Parse(Console.ReadLine());
            int height = int.Parse(Console.ReadLine());

            double resolution = width * height;
            resolution = resolution / 1000000.00;

            resolution = Math.Round(resolution, 1);

            Console.WriteLine($"{width}x{height} => {resolution}MP");
        }
    }
}
