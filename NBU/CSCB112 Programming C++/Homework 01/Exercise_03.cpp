#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{

    vector<string> keywords = {"auto", "double", "break", "else",
                               "case", "enum", "char", "extern",
                               "const", "float", "continue", "for",
                               "default", "goto", "do", "if", "int",
                               "long", "register", "return", "short",
                               "signed", "sizeof", "static", "struct",
                               "switch", "typedef", "union", "unsigned",
                               "void", "volatile", "while", "asm", "bool",
                               "catch", "class", "const_cast", "delete",
                               "dynamic_cast", "explicit", "false", "friend",
                               "inline", "mutable", "namespace", "new", "operator",
                               "private", "protected", "public", "reinterpret_cast",
                               "static_cast", "template", "this", "throw", "true", "try",
                               "typeid", "typename", "using", "virtual", "wchar_t"};

    for(auto&& x: keywords)
        cout << x << '\n';
    return 0;
}