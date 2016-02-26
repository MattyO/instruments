#include <wiringPi.h>
#include <stdio.h>

void myInterrupt (void)
{
	printf("X");
	fflush (stdout);
}
int main(int argc, char **argv)
{
	wiringPiSetup();
	pinMode(5, INPUT);
	pullUpDnControl(5, PUD_UP);
	wiringPiISR(5, INT_EDGE_SETUP, &myInterrupt);
	//printf("got here");
	fflush (stdout);

while(1){
	//printf("out%d", digitalRead(10));
	//fflush (stdout);
	//delay(500);
}

	return 0;
}
