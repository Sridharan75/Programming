#include<iostream>
using namespace std;
int main()
{
	int a,b,c;
	float Avg,Tot;
	cout<<"Enter a value for a: ";
	cin>>a;
	cout<<"Enter a value for b: ";
	cin>>b;
	cout<<"Enter a value for c: ";
	cin>>c;
	Tot=a+b+c;
	Avg=Tot/3;
	cout<<"Total= "<<Tot<<endl<<"Average= "<<Avg<<endl;
}
