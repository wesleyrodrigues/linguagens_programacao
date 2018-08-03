#include <stdio.h>

int main(void)
{
    long long int n, m, i, a;
    scanf("%lld", &n);
    scanf("%lld", &m);
    long long int array[n][m], inp[m];
    int bol = 0;
    char r[] = "0 0";

    for (i = 0; i < n; i++)
    {
        for (a = 0; a < m; a++)
        {
            scanf("%lld", &array[i][a]);
            printf("%lld\n", array[i][a]);
            if (42 == array[i][a])
            {
                bol = 1;
            }
        }
    }

    if (bol == 0)
    {
        printf(r);
    }
    else
    {
        for (i = 1; i < n - 1; i++)
        {
            for (a = 1; a < m - 1; a++)
            {
                if (array[i][a] == 42)
                {
                    if (array[i][a - 1] == 7 && array[i][a + 1] == 7)
                    {
                        if (array[i + 1][a - 1] == 7 && array[i + 1][a + 1] == 7)
                        {
                            if (array[i + 1][a] == 7 && array[i - 1][a - 1] == 7)
                            {
                                if (array[i - 1][a + 1] == 7 && array[i - 1][a] == 7)
                                {
                                    printf("%lld %lld", i + 1, a + 1);
                                    bol = 2;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    if (bol != 2 && bol != 0)
    {
        printf(r);
    }
}