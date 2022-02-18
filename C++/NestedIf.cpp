#include<iostream>
using namespace std;
int main()
{
	int m=0;
	cout<<"Enter your marks m: ";
	cin>>m;
	if (m<40){
		cout<<"Fail";
	}
	elseif(m<50){
		cout<<"Credit";
	}
	elseif(m<75){
		cout<<"merid";
	}
	else{
		cout<<"Awesome";
	}	
}
