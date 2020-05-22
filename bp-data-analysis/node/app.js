const csv = require('csv-parser');
const fs = require('fs');

const rows = []
const data = {}

// fs.createReadStream('data.csv')
//   .pipe(csv())
//   .on('data', (row) => {
//     rows.push(row)
//   })
//   .on('end', () => {
//     console.log('CSV file successfully processed');
//     console.log(rows)
//   });


let answerNumber = 1;

fs.createReadStream('testData.csv')
  .pipe(csv())
  .on('data', (row) => {
    data[answerNumber] = {};
    console.log(row)
  
  })
  .on('end', () => {
    console.log('CSV file successfully processed');
  });
