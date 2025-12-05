import requests
from datetime import datetime as dt


# -----------------------------------------------------------
#               Environment Parameters
# -----------------------------------------------------------

URL_SP_PAGE = \
    "https://www.spglobal.com/spdji/en/search/?query=index+earnings&activeTab=all"
URL_SP_XLSX = \
    "https://www.spglobal.com/spdji/en/documents/additional-material/sp-500-eps-est.xlsx"
URL_FRED_XLSX = (
    "https://fred.stlouisfed.org/graph/fredgraph.xls?bgcolor=%23e"
    "bf3fb&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23f"
    "fffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&"
    "ts=12&tts=12&width=1140&nt=0&thu=0&trc=0&show_legend=yes&"
    "show_axis_titles=yes&show_tooltip=yes&id=DFII10&scale=left&"
    "cosd=2003-01-02&coed=2025-07-01&line_color=%230073e6&"
    "link_values=false&line_style=solid&mark_type=none&mw=3&lw=3&ost=-99999&"
    "oet=99999&mma=0&fml=a&"
    "fq=Quarterly&fam=eop&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&"
    "vintage_date=2025-12-05&revision_date=2025-12-05&nd=2003-01-02")

HEADERS = \
    {"User-Agent": 
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 15_06_1) AppleWebKit/18.6 (KHTML, like Gecko) Safari/18.6"}

PRJ_ADDR = "/Users/richardkopcke/Python_Projects/sp500_earn_price_pkg/"
LOG_NAME = "chron_scrape.log"
LOG_ADDR = PRJ_ADDR + LOG_NAME

FILE_DIR = (
    "/Users/richardkopcke/Python_Projects/"
    "sp500_earn_price_pkg/input_output/input_dir/")

CURRENT_DATE = dt.strftime(dt.now(), "%Y %m %d")
SP_FILE_NAME = "sp-500-eps-est " + CURRENT_DATE + ".xlsx"

FRED_FILE_NAME = "DFII10.xlsx"


# -----------------------------------------------------------
#               Scrape/Save and iMessage
# -----------------------------------------------------------

def fetch_and_save(url, name):
    '''
    '''
    
    response = requests.get(url, headers= HEADERS)

    # True if response.status_code < 400
    # If response: ...  
    # But, here want fully successful
    if response.status_code == 200:
        with open(FILE_DIR + name, "wb+") as f:
            f.write(response.content)
    else:
        with open(LOG_ADDR, "a") as f:
            f.write(f'\tstatus code is {response.status_code} for {name}\n')
    return


# -----------------------------------------------------------
#               Chron in Main
# -----------------------------------------------------------

def main():
    '''
        In terminal, at the root
            crontab -e
            see README.md for the crontab settings
        
        This program collects and saves the files
        earn-price eliminates the redundant files before processing
    '''
    with open(LOG_ADDR, 'a') as f:
        f.write(f'chron_scrape for {CURRENT_DATE}\n')
        
    fetch_and_save(URL_SP_XLSX, SP_FILE_NAME)
    # fetch_and_save(URL_FRED_XLSX, FRED_FILE_NAME)
    
    
if __name__ == "__main__":
    main()
    