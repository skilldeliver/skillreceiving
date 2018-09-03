using System;

namespace Solution
{
  class Kata
    {
      public static int binaryArrayToNumber(int[] BinaryArray)
        {
          int sum = 0;
          for (int i = BinaryArray.Length - 1; i >= 0; i--)
          {
            if (BinaryArray[i] == 1)
            {
              sum += (int)Math.Pow(2, Math.Abs( BinaryArray.Length - 1 - i));
            }
          }
          
          return sum;
        }
    }
}