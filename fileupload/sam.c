#include<stdio.h>
#include<string.h>
int main()
{
	unsigned char c= (int)0.54;
	for(;c++;printf("%d",c));
	printf("%d",c);
	return 0;
}
