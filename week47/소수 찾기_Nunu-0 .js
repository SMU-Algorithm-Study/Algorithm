// 소수 찾기 (22.08.20)
// https://school.programmers.co.kr/learn/courses/30/lessons/42839
function primeN(n){
  if (n < 2) return false;
  for (i=2; i<=Math.sqrt(n);i++)
      if(n%i===0) return false;
  return true;
}

function solution(numbers) {
  const set = new Set();
  const nums = numbers.split('');
  
  function makeN(arr, fixN) {
    if (arr.length >= 1) {
      for (let i = 0; i < arr.length; i++) {
        let nextFixN = fixN + arr[i];
        let newArr = [...arr];
              newArr.splice(i, 1);

        if (primeN(parseInt(nextFixN))) {
          set.add(parseInt(nextFixN));
        }

        makeN(newArr, nextFixN);
      }
    }
  }
  makeN(nums, '');
  
  return set.size;
}