using System;

namespace _07._Sentence_the_Thief
{
    class Program
    {
        static void Main(string[] args)
        {
            string type = Console.ReadLine();
            long n = long.Parse(Console.ReadLine());

            long max = long.MinValue;
            long num = 0;

            if (type == "sbyte") num = sbyte.MaxValue;
            else if (type == "int") num = int.MaxValue;
            else if (type == "long") num = long.MaxValue;

            for (int i = 0; i < n; i++)
            {
                long number = long.Parse(Console.ReadLine());

                if (number > max && number <= num)
                {
                    max = number;
                }
            }

            long sentence = 0;
            if (max < 0) sentence = (long)Math.Ceiling(max / -128m);
            else sentence = (long)Math.Ceiling(max / 127m);

            if (sentence == 1 || sentence == 0) Console.WriteLine("Prisoner with id {0} is sentenced to {1} year", max, sentence);
            else Console.WriteLine("Prisoner with id {0} is sentenced to {1} years", max, sentence);

        }
    }
}

