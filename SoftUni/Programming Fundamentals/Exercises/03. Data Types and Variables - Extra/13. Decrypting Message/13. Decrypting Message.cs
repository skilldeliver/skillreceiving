using System;

namespace _13._Decrypting_Message
{
    class Program
    {
        static void Main(string[] args)
        {
            int key = int.Parse(Console.ReadLine());
            int n = int.Parse(Console.ReadLine());

            string result = "";

            for (int i = 0; i < n; i++)
            {
                int index = key;
                char chr = Console.ReadLine()[0];

                index += chr;
                result += (char)index;
            }
            Console.WriteLine(result);
        }
    }
}
