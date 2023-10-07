#include <iostream>
#include <vector>
using namespace std;


int main()
{
    int n, m, a, b;
    while (cin >> n >> m && n && m)
    {
        string linha;
        vector<string> desenho, novoDesenho;
        while (n--)
        {
            cin >> linha;
            desenho.push_back(linha);
        }
       // cin.ignore();
        cin >> a >> b;
        int escala =a/n;
        int escala2 = m-b;
        for (int s = 0; s < desenho.size(); s++)
        {
            //cout << "entrou aki" << endl;
            for (int i = 0; i < escala; i++)
            {
               // cout << "entrou aki2" << endl;

                for (int col = 0; col < escala2; col++)
                {
                  //  cout << "entrou aki3" << endl;

                    desenho[s] += desenho[s][m - 1];
                }
                novoDesenho.push_back(desenho[s]);
                novoDesenho.push_back(desenho[s]);
            }
        }
      //  cout << "saiu" << endl;

        for (int j = 0; j < novoDesenho.size(); j++)
        {
        //   cout << "ebtou" << endl;

            cout << novoDesenho[j] << endl;
        }
        cout << endl;
    }

    return 0;
}