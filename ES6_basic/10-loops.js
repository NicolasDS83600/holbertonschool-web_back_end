export default function appendToEachArrayValue(array, appendString) {
  for (const idx of array) {
    array[idx] = appendString + value;
    idx++;
  }

  return array;
}
