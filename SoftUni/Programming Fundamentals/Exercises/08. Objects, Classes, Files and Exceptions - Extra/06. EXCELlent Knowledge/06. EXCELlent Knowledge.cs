using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using Excel = Microsoft.Office.Interop.Excel;       //microsoft Excel 14 object in references-> COM tab

namespace _06._EXCELlent_Knowledge
{
    class Program
    {
        static void Main(string[] args)
        {
            Application xlApp = new Application();
            Workbook xlWorkbook = xlApp.Workbooks.Open(@"sample_table.xlsx");
            Worksheet xlWorksheet = xlWorksheets.Sheets[1];
            Range xlRange = xlWorksheet.UsedRange;

            for (int i = 1; i < 6; i++)
            {
                for (int j = 1; j < 6; j++)
                {
                    if (j == 1 && i != 1)
                    {
                        Console.WriteLine();
                    }

                    Console.Write(xlRange.Cells[i, j].Value + "|");
                }
            }

        }
    }
}
