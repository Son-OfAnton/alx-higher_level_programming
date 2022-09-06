#!/usr/bin/node
let counter = 0;
exports.logMe = function (input) {
  console.log(`${counter++}: ${input}`);
};
