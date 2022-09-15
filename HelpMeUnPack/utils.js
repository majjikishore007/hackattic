/**
 * @param {*} data
 * @description decodes the base64 data to normal form
 * @return {array} deocded data in a bytestream
 */
export const decodeData = (data) => {
  return Buffer.from(data, 'base64');
};
/**
 *
 * @param {*} byteStream
 * @return {object} message
 * @description The odrder of bytes given in the problem statement
 *
  a regular int (signed), to start off
  an unsigned int
  a short (signed) to make things interesting
  a float because floating point is important
  a double as well
  another double but this time in big endian (network byte order)
 */
export const makeData = (byteStream) => {
  const message = {
    int: byteStream.readInt32LE(0, 4),
    uint: byteStream.readUInt32LE(4, 8),
    short: byteStream.readInt16LE(8, 10),
    float: byteStream.readFloatLE(12, 16),
    double: byteStream.readDoubleLE(16, 24),
    big_endian_double: byteStream.readDoubleBE(24),
  };
  return message;
};
