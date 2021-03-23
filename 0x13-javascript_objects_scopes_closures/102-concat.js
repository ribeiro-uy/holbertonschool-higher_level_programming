#!/usr/bin/node
/*
  Task 12:
   Script that concats 2 files.
*/

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
const fs = require('fs');
// Open and save content on textFromFileA
const textFromFileA = fs.readFileSync(fileA, 'utf8');
// Open and save content on textFromFileB
const textFromFileB = fs.readFileSync(fileB, 'utf8');
// Concate in fileC
fs.writeFileSync(fileC, textFromFileA + textFromFileB);
