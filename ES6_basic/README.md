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
Modify

- function taskFirst to instantiate variables using const
- function taskNext to instantiate variables using let

```sh
export function taskFirst() {
  var task = 'I prefer const when I can.';
  return task;
}

export function getLast() {
  return ' is okay';
}

export function taskNext() {
  var combination = 'But sometimes let';
  combination += getLast();

  return combination;
}
```


### [1. Block Scope](./1-block-scoped.js)
Given what you’ve read about var and hoisting, modify the variables inside the function taskBlock so that the variables aren’t overwritten inside the conditional block.

```sh
export default function taskBlock(trueOrFalse) {
  var task = false;
  var task2 = true;

  if (trueOrFalse) {
    var task = true;
    var task2 = false;
  }

  return [task, task2];
}
```


### [2. Arrow functions](./2-arrow.js)
Rewrite the following standard function to use ES6’s arrow syntax of the function add (it will be an anonymous function after)

```sh
export default function getNeighborhoodsList() {
  this.sanFranciscoNeighborhoods = ['SOMA', 'Union Square'];

  const self = this;
  this.addNeighborhood = function add(newNeighborhood) {
    self.sanFranciscoNeighborhoods.push(newNeighborhood);
    return self.sanFranciscoNeighborhoods;
  };
}
```


### [3. Parameter defaults](./3-default-parameter.js)
Condense the internals of the following function to 1 line - without changing the name of each function/variable.

Hint: The key here to define default parameter values for the function parameters.

```sh
export default function getSumOfHoods(initialNumber, expansion1989, expansion2019) {
  if (expansion1989 === undefined) {
    expansion1989 = 89;
  }

  if (expansion2019 === undefined) {
    expansion2019 = 19;
  }
  return initialNumber + expansion1989 + expansion2019;
}
```


### [4. Rest parameter syntax for functions](./4-rest-parameter.js)
Modify the following function to return the number of arguments passed to it using the rest parameter syntax

```sh
export default function returnHowManyArguments() {

}
```


### [5. The wonders of spread syntax](./5-spread-operator.js)
File: [5-spread-operator.js](5-spread-operator.js/) - [5-main.js](5-main.js/)

Using spread syntax, concatenate 2 arrays and each character of a string by modifying the function below. Your function body should be one line long.

```sh
export default function concatArrays(array1, array2, string) {
}
```


### [6. Take advantage of template literals](./6-string-interpolation.js)
Rewrite the return statement to use a template literal so you can the substitute the variables you’ve defined.

```sh
export default function getSanFranciscoDescription() {
  const year = 2017;
  const budget = {
    income: '$119,868',
    gdp: '$154.2 billion',
    capita: '$178,479',
  };

  return 'As of ' + year + ', it was the seventh-highest income county in the United States'
        / ', with a per capita personal income of ' + budget.income + '. As of 2015, San Francisco'
        / ' proper had a GDP of ' + budget.gdp + ', and a GDP per capita of ' + budget.capita + '.';
}
```


### [7. Object property value shorthand syntax](./7-getBudgetObject.js)
Notice how the keys and the variable names are the same?

Modify the following function’s budget object to simply use the keyname instead.

```sh
export default function getBudgetObject(income, gdp, capita) {
  const budget = {
    income: income,
    gdp: gdp,
    capita: capita,
  };

  return budget;
}
```


### [8. No need to create empty objects before adding in properties](./8-getBudgetCurrentYear.js)
Rewrite the getBudgetForCurrentYear function to use ES6 computed property names on the budget object

```sh
function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
  const budget = {};

  budget[`income-${getCurrentYear()}`] = income;
  budget[`gdp-${getCurrentYear()}`] = gdp;
  budget[`capita-${getCurrentYear()}`] = capita;

  return budget;
}
```


### [9. ES6 method properties](./9-getFullBudget.js)
Rewrite getFullBudgetObject to use ES6 method properties in the fullBudget object

```sh
import getBudgetObject from './7-getBudgetObject.js';

export default function getFullBudgetObject(income, gdp, capita) {
  const budget = getBudgetObject(income, gdp, capita);
  const fullBudget = {
    ...budget,
    getIncomeInDollars: function (income) {
      return `$${income}`;
    },
    getIncomeInEuros: function (income) {
      return `${income} euros`;
    },
  };

  return fullBudget;
}
```


### [10. For...of Loops](./10-loops.js)
Rewrite the function appendToEachArrayValue to use ES6’s for...of operator. And don’t forget that var is not ES6-friendly.

```sh
export default function appendToEachArrayValue(array, appendString) {
  for (var idx in array) {
    var value = array[idx];
    array[idx] = appendString + value;
  }

  return array;
}
```


### [11. Iterator](./11-createEmployeesObject.js)
Write a function named createEmployeesObject that will receive two arguments:

- departmentName (String)
- employees (Array of Strings)

```sh
export default function createEmployeesObject(departmentName, employees) {

}
```
The function should return an object with the following format:

```sh
{
     $departmentName: [
          $employees,
     ],
}
```


### [12. Let's create a report object](./12-createReportObject.js)
Write a function named createReportObject whose parameter, employeesList, is the return value of the previous function createEmployeesObject.

```sh
export default function createReportObject(employeesList) {

}
```
createReportObject should return an object containing the key allEmployees and a method property called getNumberOfDepartments.

allEmployees is a key that maps to an object containing the department name and a list of all the employees in that department. If you’re having trouble, use the spread syntax.

The method property receives employeesList and returns the number of departments. I would suggest suggest thinking back to the ES6 method property syntax.

```sh
{
  allEmployees: {
     engineering: [
          'John Doe',
          'Guillaume Salva',
     ],
  },
};
```

---

## Author
- **Foster Clark** - [fozc](https://github.com/FosterClark48) :octocat: 
