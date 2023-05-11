// Use getFullResponseFromAPI(success) prototype to return a promise where the param is a boolean
// If success is true, return resolve({ status: 200, body: 'Success' })
// Otherwise, return reject(new Error('The fake API is not working currently'))

export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success) {
      resolve({ status: 200, body: 'Success' });
    } else {
      reject(new Error('The fake API is not working currently'));
    }
  });
}
