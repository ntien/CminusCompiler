int factorial(int x) {
  int result = 1;

  while (x > 1) {

    result = result*x;
    x = x-1;
  } else {
    return result;

  }
}

int testCond(int a, int b) {

  if (a >= b) {
    return 2*b;
  } else {
    return 3*a;
  }
}


int main() {

    int a = 1;
    int b = 2;
    int sum = a + b;

    return 0;

}   
