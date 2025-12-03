# chron_scrape
#### scrapes the S&P and FRED websites for the S&P earn-price project
#### the chron is set in the terminal

`10 10 * * * /Users/richardkopcke/.local/bin/uv run --project /Users/richardkopcke/Python_Projects/chron_scrape /Users/richardkopcke/Python_Projects/chron_scrape/main.py`

a `10 10 * * *`
- 10:10 every day

b `/Users/richardkopcke/.local/bin/uv run --project`
- specify loc of uv to launch the uv project

c `/Users/richardkopcke/Python_Projects/chron_scrape`
- location & name of the project's folder

d `/Users/richardkopcke/Python_Projects/chron_scrape/main.py`
- entry point for running the project

### NOTES
#### *https://github.com/astral-sh/uv/issues/11991*
#### *https://www.freecodecamp.org/news/vim-beginners-guide/*
#### *https://dev.to/trueqap/how-to-run-cron-on-macos-in-2025-a-complete-guide-2b8e*
#### *https://www.geeksforgeeks.org/linux-unix/cron-command-in-linux-with-examples/*
#### *https://hackernoon.com/automate-python-scripts-on-mac-a-step-by-step-guide-to-scheduling-with-crontab*

1. a uv project may be run from any directory by concatenating commands b, c, and d above.
2. `crontab -e` opens the cronjob's instruction file in a vim editor.
    - the editor opens in command mode
    - `i` opens the insert mode, which permits editing
    - `esc` returns to command mode
    - in command mode *:w* saves the file
    - ... `:q` closes the file
    - ... `:wq` saves and closes
3. spaces
    - between 10 and 10 and * and * and *
    - between a and b and c and d


