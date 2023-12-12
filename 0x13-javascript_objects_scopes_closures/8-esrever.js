#!/usr/bin/node

exports.esrever = function (list) {
  const reserverd = [];
  for (let y = list.length - 1; y >= 0; y--) {
    reserverd.push(list(y));
  }
  return (reserverd);
};
