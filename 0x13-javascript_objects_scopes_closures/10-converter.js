#!/usr/bin/node
exports.converter = function (base) {
  return conver => conver.toString(base);
};
