// Returns Promise using protoype function getResponseFromAPI()

export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    resolve();
    reject(new Error('Failed to get response from API'));
  });
}
