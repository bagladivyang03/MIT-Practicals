var fs = require('fs'); 
var http = require('http');
var formidable = require('formidable');
const axios = require('axios');
const cheerio = require('cheerio');


fs.readFile('file1.txt','utf-8',(err,data)=>{
    if(!err)
        fs.writeFile('file2.txt',data,(err)=>{
            if(err)
                throw err;
        });
    else
        throw err;
})


var readMe = fs.readFileSync('file3.txt','utf-8');
fs.writeFileSync('file4.txt',readMe);




// fs.readFile('file1.txt', 'utf-8', function(err, data) {     
//     if( !err ) 
//         fs.writeFile('file2.txt', data, (err)=>{ 
//             if( err ) { 
//                 throw err; 
//             } 
//         }); 
//     else
//         throw err; 
// }); 


  
// //synchronous
// var readMe = fs.readFileSync('file3.txt', 'utf-8');
// fs.writeFileSync('file4.txt', readMe); 
