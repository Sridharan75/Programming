#include<iostream>
using namespace std;
int main()
{
	int i=1,sum=0;
	while(i<=10){
		cout<<"i= "<<i<<"\tsum= "<<sum<<endl;
		sum+=i;
		i++;
	}
	cout<<"--And Finally--"<<endl<<"i= "<<i<<"\tsum= "<<sum<<endl;
}
