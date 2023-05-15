import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from tabulate import tabulate
from IPython.display import display


def get_page_content(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    title_name = soup.find(class_="title").get_text()
    sample_test = soup.find(class_="sample-test")
    sample_test
    input_list = []
    output_list = []
    input_tags = sample_test.find_all(class_="input")
    output_tags = sample_test.find_all(class_="output")
    for it in input_tags:
        input_list.append(it.find("pre").get_text())

    for it in output_tags:
        output_list.append(it.find("pre").get_text())
        
    
    testcases = pd.DataFrame({
        
        "input": input_list,
        "output": output_list,

    })
    
    print(title_name , url)
    print(tabulate(testcases, headers='keys',showindex=False))

   
def main():
    seed_url = "https://codeforces.com/problemset"
    print(seed_url)
    page = requests.get(seed_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    problemset = soup.find(class_="problems")
    problem_links = problemset.find_all("td",class_="id")
    url_list = []
    for data in problem_links:
        url_list.append("http://www.codeforces.com"+data.find('a').get("href"))
    print("urls crawled:",len(url_list))
    for url in url_list: 
        get_page_content(url)

if(__name__=="__main__"):
    main()
    