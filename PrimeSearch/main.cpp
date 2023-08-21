//
//  main.cpp
//  PrimeSearchAlgorithm
//
//  Created by Szymon Konieczny on 09/10/2020.
//

#include <iostream>

using namespace::std;

void printPrimes(int n);

int main() {
    int range;
    cout << "Simple program for finding prime numbers. \nUp to what number do you want to search?\n";
    
    cin >> range;
    
    
    printPrimes(range);
    
    return 0;
}


void printPrimes(int n){
    bool prime [n+1];
    
    int i;
    
    for (i = 2; i <= n; i++){
        prime[i] = true;
    }
    
    for (int divisor = 2; divisor*divisor <= n; divisor++){
        if (prime[divisor]){
            for(i = 2*divisor; i <= n; i = i+divisor){
                prime [i] = false;
            }
        }
    }
    
    for (i =2; i <= n; i++){
        if (prime[i]){
            cout << " " << i;
        }
    }
    cout << endl;
}
