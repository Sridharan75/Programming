#include<iostream>
using namespace std;
int main()
{
	int f,i,j;
	for(i=1;i<=4;i++)
	{
		cout<<"Factorial of "<<i<<" is ";
		f=1;
		for(j=1;j<=i;j++)
		{
			f=f*j;
		}
		cout<<f<<endl;
	}
}
