# ES6_basic

## Resources:books:
Read or watch:
* [ECMAScript 6 - ECMAScript 2015](https://www.w3schools.com/js/js_es6.asp)
* [Statements and declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements)
* [Arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
* [Default parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)
* [Rest parameter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)
* [Javascript ES6 — Iterables and Iterators](https://towardsdatascience.com/javascript-es6-iterables-and-iterators-de18b54f4d4)

---
## Learning Objectives:bulb:
What you should learn from this project:

- What ES6 is
- New features introduced in ES6
- The difference between a constant and a variable
- Block-scoped variables
- Arrow functions and function parameters default to them
- Rest and spread function parameters
- String templating in ES6
- Object creation and their properties in ES6
- Iterators and for-of loops

---

## Requirements
### General
- All your files will be executed on Ubuntu 18.04 LTS using NodeJS 12.11.x
- Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `js` extension
- Your code will be tested using the `Jest Testing Framework`
- Your code will be analyzed using the linter `ESLint` along with specific rules that we’ll provide
- All of your functions must be exported

---

## Setup
### Install NodeJS 12.11.x

(in your home directory):

```sh
curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
```

```sh
$ nodejs -v
v12.11.1
$ npm -v
6.11.3
```

---

## Install Jest, Babel, and ESLint

in your project directory:

- Install Jest using: npm install --save-dev jest
- Install Babel using: npm install --save-dev babel-jest @babel/core @babel/preset-env
- Install ESLint using: npm install --save-dev eslint

---

## Configuration files
### package.json

```sh

{
  "scripts": {
    "lint": "./node_modules/.bin/eslint",
    "check-lint": "lint [0-9]*.js",
    "dev": "npx babel-node",
    "test": "jest",
    "full-test": "./node_modules/.bin/eslint [0-9]*.js && jest"
  },
  "devDependencies": {
    "@babel/core": "^7.6.0",
    "@babel/node": "^7.8.0",
    "@babel/preset-env": "^7.6.0",
    "eslint": "^6.4.0",
    "eslint-config-airbnb-base": "^14.0.0",
    "eslint-plugin-import": "^2.18.2",
    "eslint-plugin-jest": "^22.17.0",
    "jest": "^24.9.0"
  }
}

```

### package.json

```sh
module.exports = {
  presets: [
    [
      '@babel/preset-env',
      {
        targets: {
          node: 'current',
        },
      },
    ],
  ],
};
```
### .eslintrc.js

```sh
module.exports = {
  env: {
    browser: false,
    es6: true,
    jest: true,
  },
  extends: [
    'airbnb-base',
    'plugin:jest/all',
  ],
  globals: {
    Atomics: 'readonly',
    SharedArrayBuffer: 'readonly',
  },
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module',
  },
  plugins: ['jest'],
  rules: {
    'no-console': 'off',
    'no-shadow': 'off',
    'no-restricted-syntax': [
      'error',
      'LabeledStatement',
      'WithStatement',
    ],
  },
  overrides:[
    {
      files: ['*.js'],
      excludedFiles: 'babel.config.js',
    }
  ]
};
```

### Finally…

Don’t forget to run npm install from the terminal of your project folder to install all necessary project dependencies.

---

### [0. Const or let?](./0-constants.js)
* Write a script that reads and prints the content of a file.


### [1. Block Scope](./1-block-scoped.js)
* Write a script that writes a string to a file.


### [2. Arrow functions](./2-arrow.js)
* Write a script that display the status code of a GET request.


### [3. Parameter defaults](./3-default-parameter.js)
* Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.


### [4. Rest parameter syntax for functions](./4-rest-parameter.js)
* Write a script that prints the number of movies where the character “Wedge Antilles” is present.


### [5. The wonders of spread syntax](./5-spread-operator.js)
* Write a script that gets the contents of a webpage and stores it in a file.


### [6. Take advantage of template literals](./6-string-interpolation.js)
* Write a script that computes the number of tasks completed by user id.


### [7. Object property value shorthand syntax](./7-getBudgetObject.js)
* Write a script that reads and prints the content of a file.


### [8. No need to create empty objects before adding in properties](./8-getBudgetCurrentYear.js)
* Write a script that writes a string to a file.


### [9. ES6 method properties](./9-getFullBudget.js)
* Write a script that display the status code of a GET request.


### [10. For...of Loops](./10-loops.js)
* Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.


### [11. Iterator](./11-createEmployeesObject.js)
* Write a script that prints the number of movies where the character “Wedge Antilles” is present.


### [12. Let's create a report object](./12-createReportObject.js)
* Write a script that gets the contents of a webpage and stores it in a file.

---

## Author
- **Foster Clark** - [fozc](https://github.com/FosterClark48):octocat:
