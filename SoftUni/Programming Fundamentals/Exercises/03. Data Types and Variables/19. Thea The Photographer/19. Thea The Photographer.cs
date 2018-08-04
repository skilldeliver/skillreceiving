using System;

namespace _19._Thea_The_Photographer
{
    class Program
    {
        static void Main(string[] args)
        {

            int n = int.Parse(Console.ReadLine());
            int filterTime = int.Parse(Console.ReadLine());
            int filterFactor = int.Parse(Console.ReadLine());
            int uploadTime = int.Parse(Console.ReadLine());

            int filtredPictures = (int)Math.Ceiling(n * filterFactor / 100.00);
            int filterPicturesTime = n * filterTime;
            int uploadTotalTime = filtredPictures * uploadTime;
            int totalTime = filterPicturesTime + uploadTotalTime;

            TimeSpan time = TimeSpan.FromSeconds(totalTime);
            Console.WriteLine("{0:D1}:{1:D2}:{2:D2}:{3:D2}s", time.Days, time.Hours, time.Minutes, time.Seconds);
        }
    }
}
