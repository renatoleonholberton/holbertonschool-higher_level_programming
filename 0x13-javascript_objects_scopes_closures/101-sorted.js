#!/usr/bin/node

const dict = require('./101-data.js').dict;

const obj = Object.entries(dict)
  .reduce((acc, [key, value]) => acc[value]
    ? { ...acc, [value]: [...acc[value], key] }
    : { ...acc, [value]: [key] }, {});

console.log(obj);
