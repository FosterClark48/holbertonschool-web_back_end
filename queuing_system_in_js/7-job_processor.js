// Task 9 - Track progress and errors with Kue: Create the Job processor

import kue from 'kue';

const blackListed = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  console.log(`Start processing job for number: ${phoneNumber}`);
  job.progress(0, 100);

  if (blackListed.includes(phoneNumber)) {
    console.log(`Failing job for blacklisted number: ${phoneNumber}`);
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

const queue = kue.createQueue();

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;

  sendNotification(phoneNumber, message, job, done);
});

queue.on('complete', (job, result) => {
  console.log(`Job ${job.id} completed`);
});

queue.on('failed', (job, err) => {
  console.log(`Job ${job.id} failed with message: ${err.message}`);
});
