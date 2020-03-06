#include <cstdio>
#include <iostream>
using namespace std;

int getBreakEvenPoint(int fixCost, int variableCost, int price) {
    int ratio = price - variableCost;
    if(ratio <= 0) return -1;
    else return (fixCost / (price - variableCost)) + 1;
}

int main() {
    int fixCost, variableCost, price;
    scanf("%d %d %d", &fixCost, &variableCost, &price);

    int result = getBreakEvenPoint(fixCost, variableCost, price);
    printf("%d", result);
}

