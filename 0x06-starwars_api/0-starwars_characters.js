#!/usr/bin/node
const request = require('request');
const filmId = process.argv[2];

if (process.argv.length !== 3) {
  console.log('Usage: ./<file> <filmId>');
  process.exit(1);
}

if (isNaN(filmId)) {
  console.error('<id> must be an integer');
  process.exit(1);
}

const reqPromise = (url) => {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
};

const printChars = async (filmId) => {
  const filmsApi = `https://swapi-api.alx-tools.com/api/films/${filmId}`;
  try {
    const filmData = await reqPromise(filmsApi);
    const characters = filmData.characters;

    const charPromises = characters.map(async (characterUrl) => {
      const charInfo = await reqPromise(characterUrl);
      return charInfo.name;
    });

    const charNames = await Promise.all(charPromises);
    charNames.forEach((name) => {
      console.log(name);
    });
  } catch (err) {
    console.error(err);
  }
};

printChars(filmId);
