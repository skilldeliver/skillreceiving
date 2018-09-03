using System;
using System.Linq;

public static class Kata
{
        public static bool IsPangram(string str)
        {
            str = str.ToLower();
            char[] alphabet = "qwertyuiopasdfghjklzxcvbnm".ToArray();
            
            for (int i = 0; i < str.Length; i++)
            {
                if (alphabet.Contains(str[i]))
                {
                    alphabet[Array.IndexOf(alphabet, str[i])] = '#';
                }
            }

            return String.Join("", alphabet) == new string('#', 26);
        }
}