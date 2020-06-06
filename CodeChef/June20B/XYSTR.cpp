//Chef and String. Link - https://www.codechef.com/JUNE20B/problems/XYSTR/
#include <iostream>
#define rli long long int
#define MOD 1000000007
#define INF 10000000000000
using namespace std;

int main() {
	int t;
	cin>>t;
	if (t>=1 && t<=100)
	{
	    while(t--)
	    {
	        string s;
	        cin>>s;
	        int counter = 0;
	        int total =0;
	        for(int i=0;i<s.length()-1;i++)
	        {
	            if (s[i]=='x' && s[i+1]=='y')
	            {
	                counter++;
	                i++;
	            }
	            else if(s[i]=='y' && s[i+1]=='x')
	            {
	                counter++;
	                i++;
	            }
	        }
	        cout<<counter<<endl;
	    }
	}
	else
	{
	    return 0;
	}
}
