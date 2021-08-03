#!/usr/bin/node

exports.esrever = function (list) {
  const lsCpy = [];

  for (const item of list) {
    lsCpy.unshift(item);
  }

  return lsCpy;
};
