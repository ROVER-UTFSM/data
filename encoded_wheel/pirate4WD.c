#include <stdio.h>
#include <wiringPi.h>

volatile int c = 0;

void count(void){
	c++;
	printf("%d\n", c);
}

int main(){
	wiringPiSetup();
	wiringPiISR(1, INT_EDGE_FALLING, &count);

	while(1);

	return 0;
}