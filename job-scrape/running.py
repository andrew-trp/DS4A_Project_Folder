#!/usr/bin/env python3 

import job_scraper
from job_scraper import find_jobs_from

desired_characs = ['titles', 'companies', 'links', 'date_listed', 'description']

find_jobs_from('Indeed', 'Data Scientist', 'new york', 50, desired_characs)
