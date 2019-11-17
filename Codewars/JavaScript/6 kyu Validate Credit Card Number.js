function validate(n){
  arr = n.toString().split('').map(Number)
 
  start = 0;
  if (arr.length % 2 == 1) start = 1
  
  for (let i = start; i < arr.length; i+=2)
  {
    arr[i] += arr[i]
    
    if (arr[i] > 9) arr[i] -= 9
  }
  
  return arr.reduce((a, b) => a + b, 0) % 10 == 0;
}