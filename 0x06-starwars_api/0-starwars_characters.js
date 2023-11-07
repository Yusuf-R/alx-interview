#!/usr/bin/node
// Write a script that prints all characters of a Star Wars movie:
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error:', response.statusCode);
    return;
  }

  const characters = JSON.parse(body).characters;
  characters.forEach((character) => {
    request(character, function (error, response, body) {
      if (error) {
        console.error(error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error('Error:', response.statusCode);
        return;
      }

      console.log(JSON.parse(body).name);
    });
  });
});
