using System;

namespace _14._Boat_Simulator
{
    class Program
    {
        static void Main(string[] args)
        {
            char firstBoat = Console.ReadLine()[0];
            char secondtBoat = Console.ReadLine()[0];
            int n = int.Parse(Console.ReadLine());

            int firstScore = 0;
            int secondScore = 0;


            for (int i = 1; i <= n; i++)
            {
                string line = Console.ReadLine();

                if (line == "UPGRADE")
                {
                    firstBoat += (char)3;
                    secondtBoat += (char)3;
                }
                else if (i % 2 != 0)
                {
                    firstScore += line.Length;
                }
                else if (i % 2 == 0)
                {
                    secondScore += line.Length;
                }

                if (firstScore >= 50)
                {
                    Console.WriteLine(firstBoat);
                    return;
                }
                if (secondScore >= 50)
                {
                    Console.WriteLine(secondtBoat);
                    return;
                }
            }

            if (firstScore > secondScore) Console.WriteLine(firstBoat);
            else Console.WriteLine(secondtBoat);

        }
    }
}
