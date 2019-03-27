const http = require("http"), 
express = require('express'),
bodyParser = require('body-parser'),
WebSocket = require('ws'),
redis = require('redis'),
redisPort = process.env.REDIS_PORT || 6379,
redisHost = process.env.REDIS_HOST || 'localhost',
reidsPassword = process.env.REDIS_PASSWORD,
redisClient = redis.createClient({port:redisPort, host: redisHost, password: reidsPassword}),
WebSocketServer = WebSocket.Server,
app = express(),
server = http.createServer(app),
port = process.env.PORT || 3000,
streamName = process.env.STREAM || 'camera:0:yolo';

app.use(bodyParser.json());
app.use(express.static('public'));

app.post('/image', function (req, res) {
	wss.clients.forEach(function each(client) {
		if (client.readyState === WebSocket.OPEN) {
			client.send(req.body.image);
		}
	});
	res.send('OK');
});


var readStream = function(){
	redisClient.xread('Block', 10000000, 'STREAMS', streamName, '$',  function (err, stream) {
		readStream();
		if(err){
			return console.error(err);	
		}
		var image = stream[0][1][0][1][1];
		wss.clients.forEach(function each(client) {
        		if (client.readyState === WebSocket.OPEN) {
        			client.send(image);
		        }
	        });
	});
};

readStream();

server.listen(port, () => console.log(`Redis Labs - app listening on port ${port}!`));

const wss = new WebSocketServer({server: server});

wss.on('connection', function (ws) {
	ws.on('message', function (message) {
		console.log('received: %s', message)
	});
});
