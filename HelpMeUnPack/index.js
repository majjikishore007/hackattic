import fetch from 'node-fetch';
import {API_KEY} from './config.js';
import {decodeData, makeData} from './utils.js';

const BaseUrl = `https://hackattic.com/challenges/help_me_unpack`;

const fetchData = async () => {
  const response = await fetch(`${BaseUrl}/problem?access_token=${API_KEY}`);
  const data = await response.json();
  return data;
};

const sendData = async (message) => {
  const response = await fetch(`${BaseUrl}/solve?access_token=${API_KEY}`, {
    method: 'POST',
    Headers: {
      'Accept': 'application.json',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(message),
  });
  const res = await response.text();
  return res;
};
const main = async () => {
  const data = await fetchData();
  const message =makeData(decodeData(data.bytes));
  const response=await sendData(message);
  console.log(response);
};
main();
