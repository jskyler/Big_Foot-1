var PORT = process.env.PORT || 5000;

var http = require('http');
var express = require('express');
const ejs = require('ejs');

var app = express();

var server = http.Server(app);

app.use(express.static('client'));

app.set('view engine', 'ejs');

server.listen(PORT, function(){
    console.log('Site is running.');
});


app.get('/', function (req, res) {
    res.render('pages/index');
});