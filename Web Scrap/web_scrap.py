from numpy import complexfloating
import requests
from bs4 import BeautifulSoup
import re
import pickle
import pprint


def load_excel_sheet(excel):
    with open(excel, 'rb') as f:
        loaded_dict = pickle.load(f)

    return loaded_dict

def get_urls(excel_dict):
    company_names = [sub['Name'].replace(' ', '-').lower() for sub in excel_dict if sub['Region'] == 'North America']
    # america_list = [for x in loaded_dict if x['Region'] == 'North America']
    # check_2_words = [name if len(name.split(' ')) == 1 else name.split(' ').  for name in company_names]
    # pprint.pprint(company_names)
    # print(len(company_names))
    base_url = "https://siccode.com/business/"
    urls = []

    for company_name in company_names:
        num_word_company_name = company_name.split('-')
        raw_url = f"{base_url}{company_name.split('-')[0]}"
        url1 = raw_url
        url2 = raw_url+"-inc"
        url3 = raw_url+"-corp"
        url4 = raw_url+"-co"
        url5 = raw_url+"-company"
        urls.extend([url1, url2, url3, url4, url5])

        if len(num_word_company_name) == 2:
            raw_url = f"{base_url}{company_name.split('-')[0] + '-' + company_name.split('-')[1]}"
            url6 =  raw_url
            url7 = raw_url+"-inc"
            url8 = raw_url+"-corp"
            url9 = raw_url+"-co"
            url10 = raw_url+"-company"
            urls.extend([url6, url7, url8, url9, url10])
        
        if len(num_word_company_name) > 2:
            raw_url = f"{base_url}{company_name.split('-')[0] + '-' + company_name.split('-')[1] + '-' + company_name.split('-')[2]}"
            url11 = raw_url
            url12 = raw_url+"-inc"
            url13 = raw_url+"-corp"
            url14 = raw_url+"-co"
            url15 = raw_url+"-company"
            urls.extend([url11, url12, url13, url14, url15])
    return urls

def read_sic_dict_pickle(file_name):
    with open(f'{file_name}.pkl', 'rb') as f:
        loaded_dict = pickle.load(f)
    return loaded_dict

def scrap(urls):
    
    for URL in urls:
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        job_elements = soup.find_all("a", class_="sic")

        for job_element in job_elements:
            span = job_element.find_all('span')
            if span != []:
                # print(str(span[0]))
                match = re.search('(?<=CODE )....', str(span[0])) # sic code 
                sic_code_first_2 = match.group(0)[:2]
                print("Company name: ", URL.split('/')[4], "SIC code: ", sic_code_first_2)

    sic_dict = read_sic_dict_pickle('data/sic_dict')
    

def main():
    excel_dict = load_excel_sheet('data/excel_data.pkl')
    urls = get_urls(excel_dict)
    print(urls)
    # scrap(urls)

if __name__ == '__main__':
    main()
