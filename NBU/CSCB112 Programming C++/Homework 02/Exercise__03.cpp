using namespace std;

int main()
{
    int a, b;

    cout << "Enter the first number: "; cin >> a;
    cout << "Enter the second number: "; cin >> b;

    a += b; a -= b; a *= b;
    a /= b; a %= b; a >>= b;
    a <<= b; a &= b; a ^= b;
    a |= b;

    return 0;
}