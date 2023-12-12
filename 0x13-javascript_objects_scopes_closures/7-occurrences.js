#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.reduce(function (con, ele) {
    return (ele === searchElement) ? con + 1 : con;
  }, 0);
};
