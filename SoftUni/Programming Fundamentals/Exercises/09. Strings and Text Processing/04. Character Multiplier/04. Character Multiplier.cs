using System;

namespace _04._Character_Multiplier
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] tokens = Console.ReadLine().Split();
            string word1 = tokens[0];
            string word2 = tokens[1];

            if (word2.Length > word1.Length)
            {
                string temp = word1;
                word1 = word2;
                word2 = temp;
            }

            long result = 0;

            for (int i = 0; i < word1.Length; i++)
            {
                if (i >= word2.Length)
                {
                    result += word1[i];
                }
                else
                {
                    result += word1[i] * word2[i];
                }
                
            }
            Console.WriteLine(result);
        }
    }
}
