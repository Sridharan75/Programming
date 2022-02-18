#include<iostream>
using namespace std;
int main(){
	int Tot=0,c=1,m=0;
	while(c<=10){
		cout<<"Enter marks m"<<c<<" :";
		cin>>m;
		Tot=Tot+m;
		c++;
	}
	cout<<"Total= "<<Tot<<endl;
}
