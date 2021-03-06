# job-scraper
### Scraping jobs from Indeed

## This repository
The module job-scraper.py enables you to web scrape job postings from Indeed.com.

Both require the package Beautiful Soup. For CWjobs, the Selenium web driver is also required. These can be installed as follows:

```
pip3 install -r requirements.txt
```

Check if you have python 3 installed (Reason for using pip3).

To use this module, import the job_scraper.py file and call the funciton "find_jobs_from()", which takes in several arguments. For an explanation and demonstration of the required arguments, see Demo.ipynb.

## To run
Set up the running.py parameters (city, job search, etc).

```
python3 running.py
```
(Might be set up as "python", just make sure you are using Python 3)

## Terms and conditions
I do not condone scraping data from Indeed or CWjobs in any way. Anyone who wishes to do so should first read their statements on scraping software [here](https://www.indeed.co.uk/legal) and [here](https://www.cwjobs.co.uk/recruiters/terms).


## Using the selenium web driver
At present, the default browser is set as Google Chrome. This can be modified within job_scraper.py.

In order to extract jobs from CWjobs using Selenium, the appropriate driver must be installed. The driver in this repository is for Google Chrome version 81. See [this link](https://sites.google.com/a/chromium.org/chromedriver/downloads) to download an appropriate driver for the Google Chrome browser, if required, and place it in the same directory as the job-scraper.py function.

## Accompanying blog post
A full description of this code and the process I followed to write it is available [here](https://medium.com/@Chris.Lovejoy/automating-my-job-search-with-python-ee2b465c6a8f).

