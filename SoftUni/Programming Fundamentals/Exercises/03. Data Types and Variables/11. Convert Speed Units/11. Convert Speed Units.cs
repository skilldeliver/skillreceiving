using System;

namespace _11._Convert_Speed_Units
{
    class Program
    {
        static void Main(string[] args)
        {
            float distance = float.Parse(Console.ReadLine());
            float hours = float.Parse(Console.ReadLine());
            float minutes = float.Parse(Console.ReadLine());
            float seconds = float.Parse(Console.ReadLine());

            seconds = (hours * 60 * 60) + (minutes * 60) + seconds;
            float metersPerSecond = distance / seconds;
            float kiometersPerHour = (distance / 1000) / (seconds / 60 / 60);
            float milesPerHour = (distance / 1000 * 0.6215040236f) / (seconds / 60 / 60);

            Console.WriteLine(metersPerSecond);
            Console.WriteLine(kiometersPerHour);
            Console.WriteLine(milesPerHour);

            // * 0.621371f

        }
    }
}
