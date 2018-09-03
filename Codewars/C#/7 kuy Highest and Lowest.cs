using System;

public class Kata
{
  public static bool IsSquare(int n)
  {
      for (int i = 0; i <= 100; i++)
      {
        if (n == i * i) return true;
      }
      
      return false;
  }
}
3 days agoRefactorDiscuss
7 kyu
Highest and Lowest
C#:
using System;
using System.Linq;

public static class Kata
{
  public static string HighAndLow(string numbers)
  {
    int max = int.MinValue;
    int min = int.MaxValue;
    
    string[] nums = numbers.Split();
    
    for (int i = 0; i < nums.Length; i++)
    {
      int n = int.Parse(nums[i]);
      
      if (n < min) min = n;
      if (n > max) max = n;
    }

    return $"{max} {min}";
  }
}