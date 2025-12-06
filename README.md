# chron_scrape
### Scrapes the S&P and FRED websites for the S&P earn-price project
### Using the terminal, add the following single line to the crontab:

`10 10 * * * /Users/richardkopcke/.local/bin/uv run --project /Users/richardkopcke/Python_Projects/chron_scrape /Users/richardkopcke/Python_Projects/chron_scrape/main.py`

a. `10 10 * * *`
- 10:10 every day

b. `/Users/richardkopcke/.local/bin/uv run --project`
- location of uv to launch the uv project

c. `/Users/richardkopcke/Python_Projects/chron_scrape`
- location of the project's folder

d. `/Users/richardkopcke/Python_Projects/chron_scrape/main.py`
- entry point for running the project

### The download from FRED does not include the TIPS rate for the current quarter. Open the DFII10.xlsx that chron_scrape adds to the input_dir and add the TIPS rate for the appropriate date.

### NOTES
#### *https://github.com/astral-sh/uv/issues/11991*
#### *https://www.freecodecamp.org/news/vim-beginners-guide/*
#### *https://dev.to/trueqap/how-to-run-cron-on-macos-in-2025-a-complete-guide-2b8e*
#### *https://www.geeksforgeeks.org/linux-unix/cron-command-in-linux-with-examples/*
#### *https://hackernoon.com/automate-python-scripts-on-mac-a-step-by-step-guide-to-scheduling-with-crontab*
#### *https://github.com/ProximaDS/python-web-file-scraper/blob/main/Web_scraperV3.py*
1. spaces
    - separate 10, 10, *, *, and *
    - separate a, b, c, and d
2. a uv project may be run from any directory by using commands b, c, and d above.
3. `crontab -e` opens the cronjob's instruction file in a vim editor.
    - the editor opens in command mode
    - `i` opens the insert mode, which permits editing
    - `esc` returns to command mode
    - in command mode, 
        - `:w` saves the file
        - `:q` closes the file
        - `:wq` saves and closes
4. in main.py, the call to fetch_and_save() for FRED's TIPS data is "commented out". The current TIPS rate must be entered separately after downloading DFII10.xlsx, and the historical TIPS rates do not change from week to week. Therefore, much of the time, there is no value in repeatedly refreshing the historical data.


