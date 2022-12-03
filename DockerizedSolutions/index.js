import fetch from 'node-fetch';
import shell from 'shelljs';

const getData = async () => {
  const response = await fetch(
    'https://hackattic.com/challenges/dockerized_solutions/problem?access_token=ab17bddaef9e90e4'
  );
  const body = await response.json();
  return body;
};
const push = async () => {
  const res = await fetch(
    'https://hackattic.com/challenges/dockerized_solutions/_/push/27e055b3.653a.448d.92ac.f4c623451d5b',
    {
      method: 'post',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        registry_host: '',
      }),
    }
  ).then((response) => {
    //do something awesome that makes the world a better place
    console.log(response);
  });
};
const main = async () => {
  // get the token and keys
  //const data = await getData();
  //const { credentials } = data;
  //console.log('data', data);
  // set up the authenation for the userr
  // push pull the image to the reqestery
  //{ user: 'gentle-smoke@hackattic.com', password: 'CPNMNY9C4H' },
  /**
     * data {
  credentials: { user: 'gentle-smoke@hackattic.com', password: 'CPNMNY9C4H' },
  ignition_key: 'OA8ZFIQMTJCUTFVHGPJFBIX5MUCK',
  trigger_token: '27e055b3.653a.448d.92ac.f4c623451d5b'
  CPNMNY9C4H


  {
credentials: {
user: "purple-pond@hackattic.com",
password: "WGP2XLWP8I"
},
ignition_key: "LEGK30MO1DALIU6WCHQXKQU96GWH",
trigger_token: "d2b87dfb.bf59.4df3.afdd.fce268ddab87"
}
}
     */

  push();
};

main();
