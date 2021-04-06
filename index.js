var PORT = process.env.PORT || 5000;

var http = require('http');
var express = require('express');
const path = require('path');
const ejs = require('ejs');

var app = express();

var server = http.Server(app);

app.use('/public', express.static(path.join(__dirname, 'public')));

app.set('view engine', 'ejs');

server.listen(PORT, function(){
    console.log('Site is running.');
});


app.get('/', function (req, res) {
    res.render('pages/index', {});
});

app.get('/maps', function(req, res) {
    res.render('pages/maps', {});
});
