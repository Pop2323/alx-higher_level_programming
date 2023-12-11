#!/usr/bin/node

const x = process.argv[2];

if (isNaN(parseInt(x))) {
    console.log('Missing size');
} else {
	for (let row = 0; row < x; row++) {
		let i = "";
		for (let col = 0; col < x; col++) {
			i += 'X';
		}
		console.log(i);
	}
}
