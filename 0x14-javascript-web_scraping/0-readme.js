#!/usr/bin/node
// Reads and prints the content of a file

const filePath = process.argv[2];
let fs = require('fs');
fs.readFile(filePath, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
