export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string' || startString.length < 1) {
    return '';
  }
  const setList = [...set];
  let newStr = '';
  for (const item of setList) {
    if (item && item.startsWith(startString)) {
      newStr = newStr.concat(item.slice(startString.length));
      newStr = newStr.concat('-');
    }
  }
  return newStr.slice(0, newStr.length - 1);
}
