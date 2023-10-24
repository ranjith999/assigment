from google.appengine.ext import web

class PrimeNumberGenerator(web.RequestHandler):
    def get(self):
        n = int(self.request.get('n'))
        primes = []
        for i in range(2, n + 1):
            if all(i % j != 0 for j in range(2, int(i**0.5) + 1)):
                primes.append(i)
        self.response.write(','.join(map(str, primes)))

app = web.app.WSGIApplication([('/primes', PrimeNumberGenerator)],
                               debug=True)

if __name__ == '__main__':
    app.run()
