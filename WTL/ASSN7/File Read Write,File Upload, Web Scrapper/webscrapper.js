const request = require('request');
const cheerio = require('cheerio');
const mongoose =  require('fs');
const { default: axios } = require('axios');

const url = "https://techdifferences.com/difference-between-normalization-and-denormalization.html";

axios(url)
    .then(response =>{
        const html = response.data;
        const $ = cheerio.load(html);
        const statsTable = $('.row-hover > tr');
        console.log(statsTable)
        const statsFinal = [];

        statsTable.each(function () {
            const parameters = $(this).find('.column-1').text();
            const normalization = $(this).find('.column-2').text();
            const denormalization = $(this).find('.column-3').text();

            statsFinal.push({                
                parameters,
                normalization,
                denormalization
            });
        });

        console.log(statsFinal)
    })
    .catch(console.error)