#!/usr/bin/node

const argc = process.argv.length;

if (argc > 2) {
  console.log('Argument' + (argc > 3 ? 's' : '') + ' found');
} else {
  console.log('No argument');
}

// const args = process.argv.slice(2);

// if (args.length == 0) {
//     console.log("No argument");
// } else if (args.length == 1) {
//     console.log("Argument found");
// } else {
//     console.log("Arguments found")
// }
