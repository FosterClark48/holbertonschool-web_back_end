export default function appendToEachArrayValue(array, appendString) {
  // Declare new variable and initialize an empty array
  const resultArray = [];
  for (const value of array) {
    // This line is called for each 'value in the 'array'.
    // It's concatenating 'appendString' and 'value', and pushing this new string into 'resultArray'
    resultArray.push(appendString + value);
  }

  return resultArray;
}
