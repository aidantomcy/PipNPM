# PipNPM

PipNPM adds functionality to create a package.json like file to add scripts
and install dependencies for Python.

Here's what a pyproject.json file should look like:

```json
{
  "name": "PipNPM",
  "description": "",
  "scripts": {
    "testScript": "echo Hello World"
  },
  "requirements": {
    "flask": "2.0.2"
  },
  "author": "Aidan Tomcy"
}
```

This project is still in the making, and if you have any ideas, please make a pull request.
