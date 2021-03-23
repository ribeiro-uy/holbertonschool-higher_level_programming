#!/usr/bin/node
/*
  Task 12:
  script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence
*/

const dict = require('./101-data.js').dict;

console.log(dict);
const newDict = {};
for (const elements in dict) {
  if (newDict[dict[elements]] === undefined) {
    newDict[dict[elements]] = [];
  }
  newDict[dict[elements]].push(elements);
}
console.log(newDict);
