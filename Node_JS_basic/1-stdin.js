// Program that listens for input from user, output's name, then displays closing message

// Display initial message
console.log('Welcome to Holberton School, what is your name?');

// Handle input
process.stdin.on('readble', () => {
  const name = process.stdin.read();
  if (name !== null) {
    process.stdout.write(`Your name is: ${input}`);
  }
});

// Handle close event
process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
