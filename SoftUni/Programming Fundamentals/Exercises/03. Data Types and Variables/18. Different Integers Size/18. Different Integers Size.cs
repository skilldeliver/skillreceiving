using System;
using System.Text;

namespace _18._Different_Integers_Size
{
    class Program
    {
        static void Main(string[] args)
        {

            string num = Console.ReadLine();
            long longTest;

            StringBuilder builder = new StringBuilder();

            if (!long.TryParse(num, out longTest))
            {
                Console.WriteLine("{0} can't fit in any type", num);
            }
            else
            {
                sbyte sbyteTest;
                if (sbyte.TryParse(num, out sbyteTest))
                    builder.Append("* sbyte").AppendLine();

                byte byteTest;
                if (byte.TryParse(num, out byteTest))
                    builder.Append("* byte").AppendLine();

                short shortTest;
                if (short.TryParse(num, out shortTest))
                    builder.Append("* short").AppendLine();

                ushort ushortTest;
                if (ushort.TryParse(num, out ushortTest))
                    builder.Append("* ushort").AppendLine();

                int intTest;
                if (int.TryParse(num, out intTest))
                    builder.Append("* int").AppendLine();

                uint uintTest;
                if (uint.TryParse(num, out uintTest))
                    builder.Append("* uint").AppendLine();

                if (long.TryParse(num, out longTest))
                    builder.Append("* long").AppendLine();

                Console.WriteLine("{0} can fit in:\n{1}", num, builder.ToString());

                // My solution dont't work because of test 6 idk i dont want to find the bug fucking disgusting judge

                //string input = Console.ReadLine();
                //try
                //{
                //    long num = long.Parse(input);

                //    Console.WriteLine(num + " can fit in:");
                //    if (num >= -128 && num < 127)
                //    {
                //        Console.WriteLine("* sbyte");
                //    }
                //    if (num >= 0 && num < 255)
                //    {
                //        Console.WriteLine("* byte");
                //    }
                //    if (num >= -32768 && num < 32767)
                //    {
                //        Console.WriteLine("* short");
                //    }
                //    if (num >= 0 && num < 65534)
                //    {
                //        Console.WriteLine("* ushort");
                //    }
                //    if (num >= -2147483648 && num < 2147483647)
                //    {
                //        Console.WriteLine("* int");
                //    }
                //    if (num >= 0 && num < 4294967295)
                //    {
                //        Console.WriteLine("* uint");
                //    }
                //    if (num >= -9223372036854775808 && num < 9223372036854775806)
                //    {
                //        Console.WriteLine("* long");
                //    }   
                //}
                //catch (System.OverflowException)
                //{
                //    Console.WriteLine(input + " can't fit in any type");
                //}
            }
        }
    }
}
