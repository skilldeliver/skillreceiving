using System;

namespace _04._Photo_Gallery
{
    class Program
    {
        static void Main(string[] args)
        {
            int photoNum = int.Parse(Console.ReadLine());
            int day = int.Parse(Console.ReadLine());
            int month = int.Parse(Console.ReadLine());
            int year = int.Parse(Console.ReadLine());
            int hour = int.Parse(Console.ReadLine());
            int minutes = int.Parse(Console.ReadLine());
            int size = int.Parse(Console.ReadLine());
            int width = int.Parse(Console.ReadLine());
            int height = int.Parse(Console.ReadLine());


            double resolution = 0.0;
            string add = "";

            if (size < 1000)
            {
                resolution = size;
                add = "B";
            }
            else if (size >= 1000 && size <= 999999)
            {
                resolution = size / 1000.00;
                add = "KB";


            }
            else if (size >= 999999)
            {
                resolution = size / 1000000.00;
                resolution = Math.Round(resolution, 1);
                add = "MB";

            }

            //double resolution = size / 1000000.00;
            //resolution = Math.Round(resolution, 1);
            string orientation = "";

            if (width == height) orientation = "square";
            else if (width > height) orientation = "landscape";
            else orientation = "portrait";

            Console.WriteLine($"Name: DSC_{photoNum:d4}.jpg");
            Console.WriteLine($"Date Taken: {day:d2}/{month:d2}/{year} {hour:d2}:{minutes:d2}");
            Console.WriteLine($"Size: {resolution}{add}");
            Console.WriteLine($"Resolution: {width}x{height} ({orientation})");
        }
    }
}
