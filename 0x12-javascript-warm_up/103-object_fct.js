#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

myObject.incr = function () {
  this.value++;
};

for (let i = 0; i < 3; i++) {
  myObject.incr();
  console.log(myObject);
}
