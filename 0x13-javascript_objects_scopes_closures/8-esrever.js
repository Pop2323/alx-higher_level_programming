#!/usr/bin/node

exports.esrever = function (list) {
  const reversed = [];
  for (let y = list.length - 1; y >= 0; y--) {
    reversed.push(list[y]);
  }
  return reversed;
};
