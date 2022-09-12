/**
 * @param {*} data
 * @description decodes the base64 data to normal form
 * @return {array} deocded data in a bytestream
 */
export const decodeData = (data) => {
  const decode = Buffer.from(data, 'base64').toJSON().data;
  return decode;
};
/**
 *
 * @param {*} byteStream
 * @return {object} message
 */
export const makeData = (byteStream) => {
  const message = {
    int: byteStream.slice(0, 4).toString(),
    uint: byteStream.slice(4, 6).toString(),
    short: byteStream.slice(6, 10).toString(),
    float: byteStream.slice(10, 14).toString(),
    double: byteStream.slice(14, 22).toString(),
    big_endian_double: byteStream.slice(22).toString(),
  };
  return message;
};
