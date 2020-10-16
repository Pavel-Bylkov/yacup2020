#include <algorithm>
#include <iostream>
#include <vector>

using std::string;
using std::cin;
using std::cout;

int** union_links(int n, int* links)
{
	int** klasters;
	int **matrix, rows, columns;
	/* инициализировать rows и columns */
	matrix = new int* [ rows ];
	for ( int i = 0; i < rows; ++i )
		matrix[i] = new int [ columns ];

	for ( int i = 0; i < rows; ++i ){
		for ( int j = 0; j < columns; ++j ){
		/* что-то сделать с matrix[i][j] */
		}
	}

	for ( int i = 0; i < rows; ++i )
		delete[] matrix[i];
	delete[] matrix;
}

int main(void)
{
	int N;
    cin >> N;
    int links[1000005][2];
	for (int i = 0; i < N; i++)
	{
		cin >> links[i][0] >> links[i][1];
	}
	int** klasters = union_links(links);
	int Q;
	cin >> Q;
	int result[1005];
	int servers[1005][101];
	for (int i = 0; i < Q; i++)
	{
		int X;
		int K;
		cin >> X >> K;
		int req[101];
		for (int j = 0; j < K; j++)
		{
			cin >> req[j];
		}
		result[i] = searchid(klasters, X, K, req);
		if (result[i] > 0)
		{
			int i = 0;
			while (i < result[i])
			{
				int j = 0;
				int n = 0;
				while (j < K)
				{
					if (req[j] > 0)
					{
						servers[i][n++] = req[j];
					}
					j++;
				}
				i++;
			}
		}
	}
    for (int i = 0; i < Q; i++)
    {
        cout << result[i];
        for (int j = 0; j < result[i]; j++)
        {
        	cout << " " << servers[i][j];
        }
        cout << "\n";
    }

    return (0);
}
