#include "iostream"
#include "stdio.h"

using namespace std;

int main() {

	int t;

	scanf("%d", &t);


	for(int i=1; i<=t; i++) {

		printf("Case %d:\n", n);

		int n, m;
		scanf("%d %d", &n, &m);

		for(int j=0;j<m;j++) {
			string s;
			cin>>s;
			long long int magicnum = n - s.length();
			long long int exp26 = 1;
			for(int k=0;k<magicnum;k++) {
				exp26 = (exp26 * 26) % 1000000007;	
			}
			printf("%lld\n", ((exp26) * (magicnum + 1)) % (1000000007));
		}
	}
	
}