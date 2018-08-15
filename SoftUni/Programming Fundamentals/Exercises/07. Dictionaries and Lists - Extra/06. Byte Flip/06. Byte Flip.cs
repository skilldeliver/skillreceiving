using System;
using System.Linq;
using System.Collections.Generic;

namespace _06._Byte_Flip
{
    class Program
    {
        static void Main(string[] args)
        {

            string[] bytes = Console.ReadLine().Split();

            List<string> bytes2 = new List<string>();

            foreach (string b in bytes)
            {
                if (b.Length == 2)
                {

                    bytes2.Add(string.Join("", b.ToCharArray().Reverse()));
                }
            }

            bytes2.Reverse();

            foreach (string b in bytes2)
            {
                Console.Write((char)int.Parse(b, System.Globalization.NumberStyles.HexNumber));
            }

        }
    }
}
