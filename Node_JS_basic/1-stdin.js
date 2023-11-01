// Program that listens for input from user, output's name, then displays closing message

// Display initial message
console.log('Welcome to Holberton School, what is your name?');

// Handle input
process.stdin.on('readable', () => {
  const name = process.stdin.read();
  if (name !== null) {
    process.stdout.write(`Your name is: ${name}`);
  }
});

// Handle close event
process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
