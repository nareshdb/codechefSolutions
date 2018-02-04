
#include <stdio.h>
#include <string>
#include <iostream>
#include <math.h>
#include <vector>
#include <sstream>

using namespace std;


//thanks - https://stackoverflow.com/questions/12975341/to-string-is-not-a-member-of-std-says-g-mingw
namespace patch
{
    template < typename T > std::string to_string( const T& n )
    {
        std::ostringstream stm ;
        stm << n ;
        return stm.str() ;
    }
}

int main() {

	long long int t;

	scanf("%lld", &t);

	while(t --> 0) {

		string s;
		cin>>s;

		vector<vector<long long int> > counts;
		std::vector<long long int> abccount;

		for(long long int i = 0; i < 26; ++i) {
			counts.push_back(vector<long long int>());
			abccount.push_back(0);
		}

		for(long long int y = 0; y < s.length(); ++y) {
			counts[int(s[y])%26].push_back(y);
			abccount[int(s[y])%26] += 1;
		}

		int	flag = 0;

		for(long long int z = 0; z < 26; ++z) {
			if (abccount[z] % 2 == 1) {
				if (s.length() % 2 == 0) {
					flag = 2;
					break;
				}
				else if(flag == 1) {
					flag = 2;
					break;
				}
				else {
					flag = 1;
				}
			}	
		}
		
		std::vector<long long int> ans;

		for(long long int i = 0; i < s.length(); ++i) {
			ans.push_back(0);
		}

		if(flag == 2) {
			printf("-1\n");
			continue;
		}
		else {
			long long int start = 0;
			long long int limit = s.length() - 1;
			for(long long int y=0 ; y < 26; ++y) {
				if((counts[y].size() % 2) == 1) {
					for(long long int i = (s.length()/2 - counts[y].size()/2), j = 0; i <= (s.length()/2 + counts[y].size()/2) ; ++i, ++j) {
						ans[i] = counts[y][j] + 1;
					}
				}
				else {
					long long int ylength = counts[y].size();
					for(long long int z = 0; z < ylength/2; ++z) {
							ans[start] = counts[y][z] + 1;
							++start;
					}
					long long int temp = limit - ylength/2;
					for(long long int z = ylength/2, i = temp+1; z < ylength; ++z, ++i) {
							ans[i] = counts[y][z] + 1;
					}
					limit = temp;
				}
			}
		}
	
		
		for(long long int i = 0; i < s.length(); ++i) {
			printf("%lld",ans[i]);
			if (i != (s.length() - 1)) {
				printf(" ");
			}
		}

		printf("\n");

	}

	return 0;
}