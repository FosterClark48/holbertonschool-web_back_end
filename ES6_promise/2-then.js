// Using prototype function handleResponseFromAPI(promise)
// Append three handlers to the function
// .then to hanlde fulfilled, .catch to handle errors, .finally to log message no matter what

export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => ({ status: 200, body: 'success' }))
    .catch(() => new Error())
    .finally(() => console.log('Got a response from the API'));
}
