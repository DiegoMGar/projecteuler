print("\nEuler project problem 2:");
print("\tEven Fibonacci numbers\n\n");

def fibonacci(n):
  lista = [1]
  if n<2: return lista;
  lista.append(2);
  for x in range(2,n):
    lista.append(lista[x-1]+lista[x-2]);
  return lista;

def fibonaccimax(n):
  lista = [1]
  if n<2: return lista;
  lista.append(2);
  x = 2;
  while True:
    value = lista[x-1]+lista[x-2];
    if value>=n:
      break;
    lista.append(value);
    x+=1;
  return lista;

def even(n):
  return n%2==0;

def evensum(n):
  result = 0;
  for x in n:
    if x%2==0:
      result+=x;
    
  return result;

#n = int(input("Fibonacci iterations: "));
#print(fibonacci(n));

n = int(input("Fibonacci max value: "));
lista = fibonaccimax(n);
#print(lista)
#print(len(lista));
#finalsum = filter(even,lista);
#print(sum(finalsum));
print(evensum(lista));
