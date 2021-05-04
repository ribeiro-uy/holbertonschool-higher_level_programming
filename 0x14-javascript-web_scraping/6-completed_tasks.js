#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (response, body) {
  const tasks = (JSON.parse(body.body));
  const tasksDone = {};
  let taskCount = 0;
  for (const task in tasks) {
    const userID = tasks[task].userId;
    if (!(userID in tasksDone)) {
      taskCount = 0;
    }
    if (tasks[task].completed === true) {
      taskCount++;
    }
    tasksDone[userID] = taskCount;
  }
  console.log(tasksDone);
});
