#include<iostream>
using namespace std;
int main()
{
	float item_price[5];
	float total=0;
	
	for(int i=0;i<5;i++){
		cout<<"Enter item "<<i+1<<" Price: Rs: ";
		cin>>item_price[i];
		total=total+item_price[i];
	}
	cout<<"\nTotal  =Rs: "<<total<<endl;
	cout<<"Average=Rs: "<<total/5<<endl;
}
