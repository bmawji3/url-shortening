# url-shortening
1. Accepts a URL and returns a shortened version.
2. Takes a shortened url and returns the original longer URL

### Terminal 1 - Start server
```
git clone https://github.com/bmawji3/url-shortening.git
cd url-shortening
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
export FLASK_APP=url_shortening_app
export FLASK_ENV=development
flask run
```

### Terminal 2 or Postman - Test Web Service
```
curl -X POST -H "Content-type: application/json" -d '{"url": "https://my-very-long-url.com/this-here-is-a-very-long-url-a-b-c-d-e-f"}' 127.0.0.1:5000/url/encode
curl -X POST -H "Content-type: application/json" -d '{"url": "https://change.co/b"}' 127.0.0.1:5000/url/decode
```

### Time Spent on Project
I spent roughly 3 hours. I was initially thinking about hashing the entire url to encode and decode, but saw some problems including the resulting hash being too long and getting frequent collisions of hashes. I also analyzed the problem from [URL shortening](https://en.wikipedia.org/wiki/URL_shortening) and gained some ideas on how to approach the problem in the `Techniques` section with the idea of base 62 conversion. Research overall took me about 1.5 hours. I spent roughly 1.5 hours more working to design, organize, and develop the web service along with testing various scenarios.
