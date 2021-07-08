#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:35:04 2020

@author: chrislovejoy
Heavily edited by: amariarv
"""
import urllib
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import re 
import time

def find_jobs_from(website, job_title, location, limit, desired_characs, filename="results.xls"):    
    """
    This function extracts all the desired characteristics of all new job postings
    of the title and location specified and returns them in single file.
    The arguments it takes are:
        - Website: to specify which website to search (options: 'Indeed' or 'CWjobs')
        - Job_title
        - Location
        - Desired_characs: this is a list of the job characteristics of interest,
            from titles, companies, links and location_listed.
        - Filename: to specify the filename and format of the output.
            Default is .xls file called 'results.xls'
    """
    
    if website == 'Indeed':
        url, page_final = urls_indeed_pages(job_title, location, limit)

        jobs_list_final = {}
        n_page = 0
        num_listings_final = 0

        while n_page < page_final:
            start = limit * n_page

            url_page = str(url)+'&start='+str(start)
            print("Working on page: ",n_page," with URL: ", url_page)

            job_soup = load_indeed_jobs_div(url_page)
            jobs_list, num_listings = extract_job_information_indeed(job_soup, desired_characs, n_page)

            df2 = pd.DataFrame(jobs_list)

            if n_page == 0:
                jobs_df = df2
            else:
                jobs_df = pd.concat([jobs_df, df2], ignore_index=True)

            num_listings_final += num_listings
            n_page += 1

            jobs_df.to_excel(filename)
            time.sleep(1500)
    #save_jobs_to_excel(jobs_df, filename)
 
    print('{} new job postings retrieved from {}. Stored in {}.'.format(num_listings_final, 
                                                                          website, filename))
    

## ======================= GENERIC FUNCTIONS ======================= ##

def save_jobs_to_excel(jobs, filename):
    jobs.to_excel(filename)

## ================== FUNCTIONS FOR INDEED.COM =================== ##

def urls_indeed_pages(job_title, location, limit):
    getVars = {'q' : job_title, 'l' : location, 'limit' : limit,'fromage' : 'last', 'sort' : 'date'}
    url = ('https://www.indeed.com/jobs?' + urllib.parse.urlencode(getVars))
    #print (url)
    page = requests.get(url,timeout=10)
    soup = BeautifulSoup(page.content, "html.parser")

    job_counter=soup.findAll("div", {"id": "searchCountPages"})[0].contents[0].split()
    print(job_counter)

    jobs_total = int(job_counter[3].replace(',', ''))

    n_page_final = int(round(jobs_total/limit,0))

    return url, n_page_final

def load_indeed_jobs_div(url_page):

    page = requests.get(url_page,timeout=10)
    soup = BeautifulSoup(page.content, 'html.parser')
    #job_soup = soup.find(id="resultsCol")
    job_soup = soup.find(id="mosaic-provider-jobcards")
   
    return job_soup

def extract_job_information_indeed(job_soup, desired_characs, n_page):

    job_elems = job_soup.findAll('a', class_=re.compile('tapItem fs-unmask result*'))

    print("Working on page:",n_page)
    cols = []
    extracted_info = []    
    
    if 'titles' in desired_characs:
        titles = []
        cols.append('titles')
        for job_elem in job_elems:
            titles.append(extract_job_title_indeed(job_elem))
        extracted_info.append(titles)                    
    
    if 'companies' in desired_characs:
        companies = []
        cols.append('companies')
        for job_elem in job_elems:
            companies.append(extract_company_indeed(job_elem))
        extracted_info.append(companies)
    
    if 'links' in desired_characs:
        links = []
        cols.append('links')
        for job_elem in job_elems:
            links.append(extract_link_indeed(job_elem))
        extracted_info.append(links)
    
    if 'location_listed' in desired_characs:
        locations = []
        cols.append('location_listed')
        for job_elem in job_elems:
            locations.append(extract_location_indeed(job_elem))
        extracted_info.append(locations)

    if 'description' in desired_characs:
        descriptions = []
        cols.append('description')
        for job_elem in job_elems:
            descriptions.append(extract_descriptions_indeed(job_elem))
        extracted_info.append(descriptions)

    jobs_list = {}
    
    for j in range(len(cols)):
        jobs_list[cols[j]] = extracted_info[j]
    
    num_listings = len(extracted_info[0])
    
    return jobs_list, num_listings


def extract_job_title_indeed(job_elem):
    URL = str(extract_link_indeed(job_elem))
    print(URL)
    page_d = requests.get(URL)
    soup_d = BeautifulSoup(page_d.content, "html.parser")
    title = soup_d.h1.text
    return title

def extract_company_indeed(job_elem):
    company = job_elem.find('span', class_="companyName").text
    return company

def extract_link_indeed(job_elem):
    link = 'https://www.indeed.com' + str(job_elem.attrs['href'])
    return link

def extract_location_indeed(job_elem):
    location = job_elem.find('div', class_="companyLocation").text
    return location

def extract_descriptions_indeed(job_elem):
    URL = str(extract_link_indeed(job_elem))
    print(URL)
    page_d = requests.get(URL)
    soup_d = BeautifulSoup(page_d.content, "html.parser")
    description = soup_d.find('div', id="jobDescriptionText")
    #description = description.text.strip()
    return description
