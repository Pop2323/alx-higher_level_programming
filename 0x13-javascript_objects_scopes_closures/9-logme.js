#!/usr/bin/node

exports.logMe = function (item) {
  let count = 0; // Declare count as a local variable
  console.log(`${count} : ${item}`);
  count++;
};
