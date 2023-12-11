#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

function findSecondLargest (numbers) {
  const sortedNumbers = numbers.sort((a, b) => b - a);
  const uniqueSortedNumbers = [...new Set(sortedNumbers)];

  if (uniqueSortedNumbers.length < 2) {
    return 0;
  }

  return uniqueSortedNumbers[1];
}

console.log(findSecondLargest(args));
