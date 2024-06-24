# 0x03. Queuing System in JS 🚀
`Back-end` `JavaScript` `ES6` `Redis` `NodeJS` `ExpressJS` `Kue`

Welcome to the `0x03. Queuing System in JS (JavaScript)` project. This `README.md` will guide you through the setup, requirements and tasks involved in building a `Redis` based queuing system using `Node.js`, `Express` and `Kue`. 🛠️
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

## Tasks 📝
### Task 0. Install a Redis instance 🛠️
**Objective**: Set up a Redis server on your local machine.

- **Steps**:
  - ✅ Download, extract, and compile the latest stable Redis version.
  - ✅ Start Redis in the background.
  - ✅ Set and get a value using `redis-cli`.
  - ✅ Copy `dump.rdb` to the project root.

**Expected Outcome**: You should have a running Redis server and be able to set/get values.

### Task 1. Node Redis Client 🔗
**Objective**: Connect to a Redis server using the `node_redis` client.

- **Requirements**:
  - ✅ Install `node_redis`.
  - ✅ Create a Redis client.
  - ✅ Log messages when the client connects or encounters an error.

**Expected Outcome**: The client should connect to the Redis server and log appropriate messages.

### Task 2. Node Redis client and basic operations ⚙️
**Objective**: Perform basic operations (set/get) with the Redis client.

- **Requirements**:
  - ✅ Create functions to set and get values from Redis.
  - ✅ Log the values retrieved from Redis.

**Expected Outcome**: You should be able to set and get values from Redis using the client.

### Task 3. Node Redis client and async operations ⏳
**Objective**: Use async/await with the Redis client for better handling of asynchronous operations.

- **Requirements**:
  - ✅ Use `promisify` from `util` to convert callback-based Redis methods to promises.
  - ✅ Create functions to set and get values asynchronously.
  - ✅ Log the values retrieved from Redis.

**Expected Outcome**: You should be able to perform asynchronous operations with Redis.

### Task 4. Node Redis client and advanced operations 🔄
**Objective**: Work with hash values in Redis.

- **Requirements**:
  - ✅ Create functions to set and get hash values.
  - ✅ Log the hash values retrieved from Redis.

**Expected Outcome**: You should be able to store and retrieve hash values in Redis.

### Task 5. Node Redis client publisher and subscriber 📡
**Objective**: Implement a publisher and subscriber using Redis.

- **Requirements**:
  - ✅ Create a subscriber that listens to a Redis channel.
  - ✅ Create a publisher that sends messages to the Redis channel.
  - ✅ Handle special messages like `KILL_SERVER` to stop the subscriber.

**Expected Outcome**: The subscriber should receive and log messages sent by the publisher.

### Task 6. Create the Job creator 🛠️
**Objective**: Create a job using Kue.

- **Requirements**:
  - ✅ Create a job queue using Kue.
  - ✅ Create a job with specific data and save it to the queue.
  - ✅ Log messages when the job is created, completed, or failed.

**Expected Outcome**: You should be able to create and track the status of a job using Kue.

### Task 7. Create the Job processor ⚙️
**Objective**: Process jobs from the queue using Kue.

- **Requirements**:
  - ✅ Create a job processor that handles jobs from the queue.
  - ✅ Log messages when a job is processed.

**Expected Outcome**: You should be able to process jobs from the queue and log their status.

### Task 8. Track progress and errors with Kue: Create the Job creator 📊
**Objective**: Track job progress and handle errors using Kue.

- **Requirements**:
  - ✅ Create multiple jobs with specific data and save them to the queue.
  - ✅ Track job progress and handle errors.
  - ✅ Log messages for job creation, completion, failure, and progress.

**Expected Outcome**: You should be able to track job progress and handle errors effectively.

### Task 9. Track progress and errors with Kue: Create the Job processor 📈
**Objective**: Implement a job processor that tracks progress and handles errors.

- **Requirements**:
  - ✅ Create a job processor that handles jobs from the queue.
  - ✅ Track job progress and handle errors.
  - ✅ Log messages for job processing, progress, and errors.

**Expected Outcome**: You should be able to process jobs, track their progress, and handle errors effectively.
<br></br>

---
## Tips 💡
- Be sure to test each task to verify functionality.
- For asynchronous operations, handle errors properly to avoid crashing the app.
- Utilize `kue`'s built-in event listeners (`complete`, `failed`, `progress`) to track the state of jobs.
<br></br>

---
## Author ✨
- **Ernest Bhekizwe Shongwe** - [GitHub](https://github.com/bshongwe)
<br></br>

---
## License 📜
This project is licensed under the ISC License

---
Happy coding! 🚀
