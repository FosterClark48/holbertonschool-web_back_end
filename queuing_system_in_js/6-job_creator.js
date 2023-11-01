// Task 6 - Create the Job Creator

import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
};

const job = queue.create('push_notification_code', jobData).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});

// Completed listener
job.on('complete', () => {
  console.log('Notification job completed');
});

// Failed listener
job.on('failed', (err) => {
  console.log('Notification job failed');
});
