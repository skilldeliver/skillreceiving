using System;

namespace _05._BPM_Counter
{
    class Program
    {
        static void Main(string[] args)
        {
            int bpm = int.Parse(Console.ReadLine());
            int beats = int.Parse(Console.ReadLine());

            double coef = (double) beats / bpm;
            double perMin = Math.Truncate(coef);
            
            double perSec = coef - perMin;
            perSec *= 100;
            perSec *= 0.6;
            double bars = beats / 4.0;
            bars = Math.Round(bars, 1);
            perSec = Math.Truncate(perSec);

            Console.WriteLine($"{bars.ToString("#.#")} bars - {perMin}m {perSec}s");
        }
    }
}
