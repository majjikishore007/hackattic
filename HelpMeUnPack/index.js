import fetch from 'node-fetch';
fetch("https://hackattic.com/challenges/help_me_unpack/problem?access_token=ab17bddaef9e90e4")
  .then((response) => response.json())
  .then(data=>{console.log(data)})