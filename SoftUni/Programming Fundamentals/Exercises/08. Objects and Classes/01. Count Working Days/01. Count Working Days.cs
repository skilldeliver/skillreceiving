using System;
using System.Linq;
using System.Collections.Generic;
using System.Globalization;

namespace _08._Objects_and_Classes___Exercises
{
    class Program
    {
        static void Main(string[] args)
        {
            DateTime[] holidays = new DateTime[12];
            holidays[0] = new DateTime(4, 01, 01);
            holidays[1] = new DateTime(4, 03, 03);
            holidays[2] = new DateTime(4, 05, 01);
            holidays[3] = new DateTime(4, 05, 06);
            holidays[4] = new DateTime(4, 05, 24);
            holidays[5] = new DateTime(4, 09, 06);
            holidays[6] = new DateTime(4, 09, 22);
            holidays[7] = new DateTime(4, 11, 01);
            holidays[9] = new DateTime(4, 12, 24);
            holidays[10] = new DateTime(4, 12, 25);
            holidays[11] = new DateTime(4, 12, 26); 

            DateTime start = DateTime.ParseExact(Console.ReadLine(), "dd-MM-yyyy", CultureInfo.InvariantCulture);
            DateTime end = DateTime.ParseExact(Console.ReadLine(), "dd-MM-yyyy", CultureInfo.InvariantCulture);

            int count = 0;
            bool skip = false;

            for (DateTime date = start; date <= end; date = date.AddDays(1))
            {
                DayOfWeek day = date.DayOfWeek;

                DateTime temp = new DateTime(4, date.Month, date.Day);

                if (!holidays.Contains(temp) && (!day.Equals(DayOfWeek.Saturday) && !day.Equals(DayOfWeek.Sunday)))
                {
                    count++;
                }
            }
            Console.WriteLine(count);

        }

    }
}

