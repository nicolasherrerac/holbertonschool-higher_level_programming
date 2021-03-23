#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((c, e) => e === searchElement ? c + 1 : c, 0);
};
