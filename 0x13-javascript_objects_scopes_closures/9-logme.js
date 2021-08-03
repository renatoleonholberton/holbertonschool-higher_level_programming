#!/usr/bin/node

exports.logMe = function (item) {
  if (!this.argsCount) {
    this.argsCount = 0;
  }

  console.log(`${this.argsCount++}: ${item}`);
};
