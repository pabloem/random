#include <stdio.h>

void print_variable(char *variable)
{
  printf("Variable is %d\n",*variable);
}

int main()
{
  int variable = 1;
  print_variable((char *) &variable);
}
