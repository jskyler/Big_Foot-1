var PORT = process.env.PORT || 5000;

var http = require('http');
var express = require('express');
const ejs = require('ejs');

var app = express();

var server = http.Server(app);


app()
    .use(express.static(path.join(__dirname, 'public')))
    .set('views', path.join(__dirname, 'views'))
    .set('view engine', 'ejs')
    .get('/', (req, res) => res.render('pages/index'))
    .listen(PORT,() => console.log(`Listening on ${ PORT }`))