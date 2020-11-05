//
// Created by VM on 20-Nov-19.
//

#ifndef NBU_UTILITIES_H
#define NBU_UTILITIES_H

#endif //

#include <iostream>
#include <vector>
#include <string>

using namespace std;


// TEXT PROCESSING

// DON'T FORGET TO getline(cin, text);


vector<string> split_text(string text)
{
    vector<string> sentence;

    string word = "";
    for (auto x : text) {
        if (x == ' ') {
            if (word != "") sentence.push_back(word);
            word = "";
        } else {
            word = word + x;
        }
    }
    if (word != "") sentence.push_back(word);
    return sentence;
}


// MATRIX INPUT, PRINTING


// DYNAMIC MATRIX INPUT
void input_dynamic()
{
    unsigned n, m;

    cout << "Enter the number of rows: ";
    cin >> m;
    cout << "Enter the number of columns";
    cin >> n;

    int* *arr = new int*[m];

    for (int i = 0; i <= m - 1; ++i) {
        arr[i] = new int[n];
    }

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            cout << ">>>";
            cin >> arr[i][j];
        }
    }

    for (int i = 0; i < m; i++)
        delete [] arr[i];
    delete [] arr;
    arr = NULL;
}



// SPIRAL PRINT TOP-BOT -> LEFT-RIGHT -> BOT-TOP -> RIGHT-LEFT

void print_spiral(int end_row, int end_col, int arr[R][C])
{
    int row = 0, col = 0;

    while (row < end_row && col < end_col) {

        for (int i = row; i < end_row; i++) {
            cout << arr[i][col] << " ";
        }
        col++;

        for (int i = col; i < end_col; i++)
        {
            cout << arr[end_row - 1][i] << " ";
        }
        end_row--;

        if (col < end_col)
        {
            for (int i = end_row - 1; i >= row; i--)
            {
                cout << arr[i][end_col - 1] << " ";
            }
            end_col--;
        }

        if (row < end_row)
        {
            for (int i = end_col - 1; i >= col; i--)
            {
                cout << arr[row][i] << " ";
            }
            row++;
        }

    }
}

vector<int> print_spiral(int end_row, int end_col, int arr[R][C])
{
    int row = 0, col = 0;
    vector<int> spiral;

    while (row < end_row && col < end_col) {

        for (int i = row; i < end_row; i++) {
            spiral.push_back(arr[i][col] << " ";
        }
        col++;

        for (int i = col; i < end_col; i++)
        {
            spiral.push_back(arr[end_row - 1][i]);
        }
        end_row--;

        if (col < end_col)
        {
            for (int i = end_row - 1; i >= row; i--)
            {
                spiral.push_back(arr[i][end_col - 1]);
            }
            end_col--;
        }

        if (row < end_row)
        {
            for (int i = end_col - 1; i >= col; i--)
            {
                spiral.push_back(arr[row][i]);
            }
            row++;
        }
    }
    return spiral;


// RANDOMIZING NUMBERS

// DON'T FORGET TO SEED -> srand(time(NULL)); AND ->
/*
   #include <random>
   #include <ctime>
 */

    double rand_num(double min, double max)
    {
        rand();
        return min + ((double)rand() / RAND_MAX) * (max - min);
    }

    int rand_num(int min, int max)
    {
        return rand() % (max - min) + min;
    }

}
