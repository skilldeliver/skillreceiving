using System;
using System.Collections.Generic;

namespace _05._Parking_Validation
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            Dictionary<string, string> data = new Dictionary<string, string>();
            
            for (int i = 0; i < n; i++)
            {
                string[] info = Console.ReadLine().Split();

                if (info[0] == "register")
                {
                    if (data.ContainsKey(info[1]))
                    {
                        Console.WriteLine("ERROR: already registered with plate number " + data[info[1]]);
                        continue;
                    }
                    if (UnvalidFormat(info[2]))
                    {
                        Console.WriteLine("ERROR: invalid license plate " + info[2]);
                        continue;
                    }
                    if (UnvalidLicense(data, info[2]))
                    {
                        Console.WriteLine($"ERROR: license plate {info[2]} is busy");
                        continue;
                    }

                    Console.WriteLine($"{info[1]} registered {info[2]} successfully");
                    data[info[1]] = info[2];
                }
                else
                {
                    if (data.ContainsKey(info[1]))
                    {
                        data.Remove(info[1]);
                        Console.WriteLine($"user {info[1]} unregistered successfully");
                    }
                    else
                    {
                        Console.WriteLine($"ERROR: user {info[1]} not found");
                    }
                }
            }

            foreach (var entry in data)
            {
                Console.WriteLine($"{entry.Key} => {entry.Value}");
            }
        }

        static bool UnvalidLicense(Dictionary<string, string> data, string license)
        {
            foreach (string val in data.Values)
            {
                if (val == license)
                {
                    return true;
                }
            }
            return false;

        }

        static bool UnvalidFormat(string license)
        {
            string num = license.Substring(2, 4);

            if (license.Length == 8 && long.TryParse(num, out long n) && IsUpper(license.Substring(0, 2)) && IsUpper(license.Substring(6, 2)))
            {
                return false;
            }
            return true;

        }

        static bool IsUpper(string str)
        {
            for (int i = 0; i < str.Length; i++)
            {
                if (!Char.IsUpper(str[i]))
                    return false;
            }

            return true;
        }
    }
}
