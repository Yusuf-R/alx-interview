#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

function makeRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, function (error, response, body) {
      if (error) {
        reject(new Error(error)); // Pass an Error object as the rejection reason
      } else if (response.statusCode !== 200) {
        reject(new Error('Error: ' + response.statusCode)); // Pass an Error object as the rejection reason
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

async function fetchCharacters () {
  try {
    const filmData = await makeRequest(url);
    const characters = filmData.characters;

    for (const character of characters) {
      const characterData = await makeRequest(character);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error(error);
  }
}

fetchCharacters();
