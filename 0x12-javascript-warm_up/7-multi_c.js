#!/usr/bin/node
const freq = parseInt(process.argv[2]);
if (isNaN(freq)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < freq; i++) {
    console.log('C is fun');
  }
}
