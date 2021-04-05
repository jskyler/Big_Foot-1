var PORT = process.env.PORT || 5000;

var http = require('http');
var express = require('express');
var app = express();

var server = http.Server(app);

app.use(express.static('client'));

server.listen(PORT, function(){
    console.log('Site is running.');
});
