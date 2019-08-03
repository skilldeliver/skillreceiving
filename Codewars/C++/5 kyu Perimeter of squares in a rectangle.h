typedef unsigned long long ull;
class SumFct
{
public:
    static ull perimeter(int n)
    {
        ull last = 0;
        ull fib_num = 1;
        ull fib_sum = 0;
        for (int i = 0; i <= n; ++i) {
            fib_sum += fib_num;
            fib_num = fib_num + last;
            last = fib_num - last;

        }
        return 4 * fib_sum;
    };
};
