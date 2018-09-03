using System;
using System.Linq;
using System.Collections.Generic;

public class Kata
{
  public static string SpinWords(string sentence)
  {
      string[] words = sentence.Split();
      
      for (int i = 0; i < words.Length; i++)
      {
        if (words[i].Length > 4)
        {
          words[i] = String.Join("", words[i].Reverse().ToList());
        }
      }
      
      return String.Join(" ", words);
  }
}