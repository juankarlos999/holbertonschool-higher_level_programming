#!/usr/bin/node
const arg = parseInt(process.argv[2]);
if (isNaN(arg)) console.log('Missing size');
for (let colum = 0; colum < arg; colum++) console.log('X'.repeat(arg));
