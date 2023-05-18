export default function hasValuesFromArray(set, array) {
  return array.every((number) => set.has(number));
}
