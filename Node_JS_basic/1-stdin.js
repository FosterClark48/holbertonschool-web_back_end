// Program that listens for input from user, output's name, then displays closing message

const readline = require('readline');

// Create interface for readline
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Display initial message
console.log('Welcome to Holberton School, what is your name?');

// Handle input
rl.on('line', (input) => {
  console.log(`Your name is: ${input}`);
  rl.close();
});

// Handle close event
rl.on('close', () => {
  console.log('This important software is now closing');
});
