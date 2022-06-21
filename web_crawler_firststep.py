
import requests
url = 'https://www.indeed.com/jobs?q=machine%20learning&l&from=searchOnHP&vjk=b482a789d0c3e539'

req = requests.get(url)

webpage = req.text


from bs4 import BeautifulSoup

soup = BeautifulSoup(webpage, 'html.parser')


head = "https://www.indeed.com/"
def get_job_links_from_page(url):
    """
    This function gets the links of the jobs on the joblist page.

    Args:
        url (str): link to joblist page

    Returns:
        job_page_links (list): list of links to the webpages of the jobs
    """

    job_page_links = []
    soup = BeautifulSoup(webpage, 'html.parser')
    for item in soup.find_all("a", href=True):
        if '/rc/clk?jk=' in str(item) and 'fccid=' in str(item):
            link = item['href'].split("clk?")[1]
            job_page_links.append(head+'viewjob?'+link)
    return job_page_links


links = get_job_links_from_page(url)


import pandas as pd
df = pd.DataFrame(links)


import os  
os.makedirs('Desktop/Techlent', exist_ok=True)  
df.to_csv('Desktop/Techlent/Sample_data.csv') 

