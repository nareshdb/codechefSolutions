#include <stdio.h>
#include <string>
#include <iostream>
#include <math.h>

using namespace std;

int main() {

	int t;

	cin>>t;

	while(t --> 0) {
		int N, M, X, K;
		string s;

		cin>>N>>M>>X>>K>>s;

		int evenCount = 0, oddCount = 0;

		for(int i = 0 ; i < s.length() ; ++i) {
			if (s[i] == 'E') {
				++evenCount;
			}
			else {
				++ oddCount;
			}
		}
		
		if ((M == 0) || (X == 0) || (N > K)) {
			printf("no\n");
			continue;
		}

		int noOfEvenMonths = M/2;
		int noOfOddMonths = ceil(float(M)/2.0);

		if( N <= (min((noOfEvenMonths * X), evenCount) + min((noOfOddMonths * X), oddCount)) )
			printf("yes\n");
		else
			printf("no\n");
	}
}