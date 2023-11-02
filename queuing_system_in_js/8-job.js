// Task 10 - Writing the job creation function

const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  for (const job of jobs) {
    const jobNew = queue.create('push_notification_code_3', job).save();

    try {
      jobNew.on('enqueue', () => {
        console.log(`Notification job created: ${jobNew.id}`);
      }).on('complete', () => {
        console.log(`Notification job ${jobNew.id} completed`);
      }).on('failed', (err) => {
        console.log(`Notification job ${jobNew.id} failed: ${err}`);
      }).on('progress', (progress) => {
        console.log(`Notification job ${jobNew.id} ${progress}% complete`);
      });
    } catch (err) { }
  }
};

module.exports = createPushNotificationsJobs
