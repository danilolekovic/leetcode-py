# leetcode-web

A template repository for Leetcode webpage generation. See an example at [my personal webpage](https://danilolekovic.github.io/leetcode/index.html).

## features

- Generates webpage with all of your Leetcode solutions
- Syntax highlighting

## requirements

- Node.js

## usage

- Fork or clone this repository with gh-pages as your branch. `git clone https://github.com/danilolekovic/leetcode-web.git`
- Edit `info.json`, include your own first name or username, or change "Leetcode" to "Hackerrank" or whatever you're using
- Create folders (use - instead of spaces), this will be the name of the problem
- Put your problems in files called `solution.js` or `solution.cpp` or whichever programming language you are using (currently supporting Python, JavaScript, MySQL, C, C++, Ruby, Java)
- Run `node build.js`
- Push to GitHub