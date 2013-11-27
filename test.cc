
#include <iostream>

using namespace std;

int main(){
int counter1=0;
int counter2=0;
for(int i=0; i<1000; i++){
   if(i%3==0 || i%5==0) counter1+=i;
    }
   cout << counter1 << endl;

}
