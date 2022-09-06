#!/usr/bin/node
exports.nbOccurences = function (array, target) {
  let counter = 0;
  for (let i = 0; i < array.length; i++) {
    if (array[i] === target) {
      counter += 1;
    }
  }
  return counter;
};
