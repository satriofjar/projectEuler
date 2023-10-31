#include <bits/stdc++.h>
using namespace std;

int sol1(int lim){
	int res = 0;
	for(int i= 1;i < lim;i ++){
		if (i % 3 == 0 || i % 5 == 0)
			res += i;
	}
	return res;
}

int sol2(int lim){
	int res = 0,a = 1, b=1;
	int temp;
	while(a < lim){
		if (a % 2 == 0)
			res += a;
		
		temp = a;
		a = b;
		b = temp + b;
	}
	
	return res;
}

// problem 2 with recurtion
int sol2a(int a, int b, int res, int lim){
	if(a > lim)
		return res;
	else
		if(a % 2 == 0)
			res += a;
		return sol2a(b, a + b, res, lim);
}

bool is_even(int x){
	if(x % 2 == 0)
		return true;
	else
		return false;
}

bool is_prime(int x){
	double akar = round(sqrt(x));
	if(x < 2)
		return false;
	else if(x == 2)
		return true;
	else if(is_even(x))
		return false;
	else
		for(int i=3;i<akar + 1; i+= 2){
			if(x % i == 0)
				return false;
		}
		return true;
}

int sol3(long long x){
	int akar = round(sqrt(x));
	int res = 0;
	
	if(is_prime(x))
		return x;
	
	for(int i=3; i < akar + 1; i += 2){
		if(is_prime(i))
			if(x % i == 0)
				res = i;
	}
	
	return res;
}

int main(){
	cout << sol3(600851475143) << endl;
	return 0;
}