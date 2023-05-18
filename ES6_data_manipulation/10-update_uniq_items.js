export default function updateUniqueItems(inputMap) {
  if (!(inputMap instanceof Map)) {
    throw new Error('Cannot process');
  }

  inputMap.forEach((key, value) => {
    if (key === 1) {
      inputMap.set(value, 100);
    }
  });

  return inputMap;
}
