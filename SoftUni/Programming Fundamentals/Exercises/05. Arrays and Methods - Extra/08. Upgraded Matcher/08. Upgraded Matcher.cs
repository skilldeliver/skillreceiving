using System;
using System.Linq;

namespace _08._Upgraded_Matcher
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] products = Console.ReadLine().Split(' ');
            long[] quanities = Console.ReadLine().Split(' ').Select(long.Parse).ToArray();
            decimal[] price = Console.ReadLine().Split(' ').Select(decimal.Parse).ToArray();

            string line = "";
            while (line != "done")
            {
                line = Console.ReadLine();

                if (line != "done")
                {
                    string product = line.Split(' ')[0];
                    long quanity = long.Parse(line.Split(' ')[1]);

                    long index = Array.IndexOf(products, product);

                    long currQuanity = 0;
                    try
                    {
                        currQuanity = quanities[index];
                    }
                    catch (IndexOutOfRangeException) { }
                    

                    if (quanity > currQuanity)
                    {
                        Console.WriteLine("We do not have enough " + product);
                    }
                    else
                    {
                        try
                        {
                            quanities[index] -= quanity;
                        }
                        catch (IndexOutOfRangeException) { }

                        Console.WriteLine($"{product} x {quanity} costs {quanity * price[index]:F2}");
                    }
                }
            }
        }
    }
}
