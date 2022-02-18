#include<iostream>
using namespace std;
int main(){
	int x,y,z;
	int *a,*b,*c;
	x=5,y=10,z=15;
	a=&x;
	b=&y;
	c=&z;
	c=a,a=b,b=c;
	*c=*c+5;
	cout<<x<<","<<y<<","<<z;
}
