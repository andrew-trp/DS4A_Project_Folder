#!/usr/bin/env python3 
import time
import job_scraper_new
from job_scraper_new import find_jobs_from

desired_characs = ['titles', 'companies', 'links', 'location_listed', 'description']

company_array = ["amazon", "microsoft", "IBM", "oracle"]

city_array = ["Austin, TX","Phoenix, AZ","Seattle, WA", "Miami, FL", "San Francisco, CA", "Denver, CO", "New York City, NY", "Boston, MA"]
city_file_array = ["Austin","Phoenix","Seattle", "Miami", "San_Francisco","Denver","NY", "Boston"]

for n in [7]:
    print(city_array[n], city_file_array[n])
    find_jobs_from('Indeed', 'Data Scientist', city_array[n], 50, desired_characs, str(city_file_array[n])+"_all.xls")
    time.sleep(1800)
"""

for n in company_array:
    print(n)
    find_jobs_from('Indeed', 'Data Scientist '+str(n), "US", 50, desired_characs, str(n)+".xls")

"""
