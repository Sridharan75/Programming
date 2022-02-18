#include<iostream>
using namespace std;
int main()
{
	char m;
	cout<<"Enter your Grade: ";
	cin>>m;
	switch(m)
	{
		case 'A':
			cout<<"Excelent";
			break;
		case 'B':
			cout<<"Average Pass";
			break;
		case 'F':
			cout<<"Fail";
			break;
		default:
			cout<<"Invalid Grade.";
	}
}
