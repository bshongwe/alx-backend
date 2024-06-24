# 0x03. Queuing System in JS 🚀
`Back-end` `JavaScript` `ES6` `Redis` `NodeJS` `ExpressJS` `Kue`

Welcome to the `0x03. Queuing System in JS (JavaScript)` project. This
`README.md` will guide you through the setup, requirements and tasks involved
in building a `Redis` based queuing system using `Node.js`, `Express` and
`Kue`. 🛠️
<br></br>

## Resources 📚
### Read or watch:
- [Redis quick start](https://redis.io/docs/getting-started/)
- [Redis client interface](https://redis.io/topics/rediscli)
- [Redis client for Node JS](https://github.com/redis/node-redis)
- [Kue (deprecated but still in use)](https://github.com/Automattic/kue)
<br></br>

## Learning Objectives 🎯
By the end of this project, you will be able to:
- Run a Redis server on your machine
- Perform basic Redis operations
- Use a Redis client with Node.js
- Store hash values in Redis
- Handle asynchronous operations with Redis
- Implement Kue as a queue system
- Build a basic Express app that interacts with Redis
- Create a basic Express app that interacts with Redis and a queue
<br></br>

## Requirements 📋
- Code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7
- All files should end with a new line
- A README.md file at the root of the project is mandatory
- Use `.js` extension for your code files
<br></br>

## Required Files 📂
### `package.json`
This file is used to manage project dependencies and scripts.
```json
{
  "name": "queuing_system_in_js",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "dev": "nodemon --exec babel-node --presets @babel/preset-env"
  },
  "dependencies": {
    "babel-cli": "^6.26.0",
    "babel-preset-env": "^1.7.0",
    "kue": "^0.11.6",
    "redis": "^3.1.2"
  }
}
```
<br></br>

### `.babelrc`
This file is used to configure Babel to use the `@babel/preset-env` preset.
```json
{
  "presets": ["@babel/preset-env"]
}
```
<br></br>

### Installation

Run the following command to install project dependencies:
```bash
$ npm install
```
<br></br>

# Tasks 📝

| Task | Description |
|------|-------------|
| **Task 0:** Install a Redis instance 🛠️ | Set up a Redis server on your local machine. |
| **Task 1:** Node Redis Client 🔗 | Connect to a Redis server using the `node_redis` client. |
| **Task 2:** Node Redis client and basic operations ⚙️ | Perform basic operations (set/get) with the Redis client. |
| **Task 3:** Node Redis client and async operations ⏳ | Use async/await with the Redis client for better handling of asynchronous operations. |
| **Task 4:** Node Redis client and advanced operations 🔄 | Work with hash values in Redis. |
| **Task 5:** Node Redis client publisher and subscriber 📡 | Implement a publisher and subscriber using Redis. |
| **Task 6:** Create the Job creator 🛠️ | Create a job using Kue. |
| **Task 7:** Create the Job processor ⚙️ | Process jobs from the queue using Kue. |
| **Task 8:** Track progress and errors with Kue: Create the Job creator 📊 | Track job progress and handle errors using Kue. |
| **Task 9:** Track progress and errors with Kue: Create the Job processor 📈 | Implement a job processor that tracks progress and handles errors. |
| **Task 10:** Create Push Notifications Jobs 📲 | Create push notification jobs using Kue. |
| **Task 11:** Test Push Notifications Jobs 🧪 | Write tests for the push notification jobs using Sinon and Chai. |
| **Task 12:** Stock Management API 📦 | Build an API for managing stock using Express and Redis. |
| **Task 13:** Seat Reservation System 🪑 | Implement a seat reservation system using Express, Redis, and Kue. |

<br></br>

## Tips 💡
- Be sure to test each task to verify functionality.
- For asynchronous operations, handle errors properly to avoid crashing the
app.
- Utilize `kue`'s built-in event listeners (`complete`, `failed`, `progress`)
to track the state of jobs.
<br></br>

---
## Author ✨
- **Ernest Bhekizwe Shongwe** - [GitHub](https://github.com/bshongwe)
<br></br>

## License 📜
This project is licensed under the ISC License

---
Happy coding! 🚀
