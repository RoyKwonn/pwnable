#include <string.h>
#include <stdio.h>

void func2() {
	puts("func2()");
}

void sum(int a, int b){
	printf("sum : %d\n", a+b);
	func2();
}

int main(int argc, char *argv[]){
	int num=0;
	char arr[10];

	sum(1,2);
	strcpy(arr,argv[1]);
	printf("arr: %s\n", arr);
	if(num==1){
		system("/bin/sh");
	}
	return 0;
}
