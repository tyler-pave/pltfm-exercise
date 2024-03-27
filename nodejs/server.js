import express from 'express';
import morgan from 'morgan';
import { nanoid } from 'nanoid';
const app = express()
const port = 3000

/*
We want to build a simple URL shortener server.

Two main endpoints:

POST /create:
- takes a longUrl as a body parameter
- returns a shortCode

GET /go/:shortCode
- takes a shortCode URL parameter
- returns (or redirects to) the saved longUrl

Stage 1: Store in memory. Will implement.
Stage 2: Cache in Redis. Will discuss, may partially implement.
Stage 3: Add in SQLite or other SQL DB. Will discuss, but will not implement.
Stage 4: Further optimizations and enhancements. Will discuss, but will not implement.

Potential additional functionality:
- On creation, if we already have a shortCode for a given longUrl, just return the existing shortCode
- Allow a user to specify a desired shortCode on creation
- Track how many times a shortCode has been visited
- Performance optimizations
- Deployment scenarios

*/

const shortCodes = {}

app.use(morgan('combined'));
app.use(express.urlencoded({ limit: '10kb', extended: false }));

app.get('/', (req, res) => {
  res.send(`
    <form action="/create" method="post">
      <input type="text" name="longUrl">
      <input type="submit">
    </form>
  `);
});

app.post('/create', (req, res) => {
  // Get a longUrl body param, store it, return a shortCode
});

app.get('/go/:shortCode', (req, res) => {
  // Look up the shortCode, return the longUrl
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
});
