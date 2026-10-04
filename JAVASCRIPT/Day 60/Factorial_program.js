function factorialCalculator(num) {
  let result = 1;
  for (let i = num; i > 1; i--) {
    result = result * i;
  }
  return result;
}

let num = 4;
let factorial = factorialCalculator(num);
console.log(`Factorial of ${num} is ${factorial}`);
