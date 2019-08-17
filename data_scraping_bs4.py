from bs4 import BeautifulSoup
import requests
import csv


def main():

    # first inspect the html of the website
    start_date = r'2017-06-01'
    end_date = r'2018-06-01'
    page_number = r'1'
    url = r'http://www.buffalo.oarsystem.com/assessment/results.asp?swis=140200&rptname=rpt&page={p}&cnty=&urlparm=swis=140200&cnty=&tbox=&tbox=&startdate={s}&enddate={e}&lwrsaleprice=&uprsaleprice=&lwrasmt=&uprasmt=&oname1=&lwryrbuilt=&upryrbuilt=&lwrsqft=&uprsqft=&lwrbdrms=&uprbdrms=&lwrbaths=&uprbaths=&lwrfrplcs=&uprfrplcs=&searchtype=Sales&nghdcode=&prop_class=&sch_code=&hstyle=&waterfr_type=&rswis=&overall_desire=&stname='.format(s=start_date,e=end_date,p=page_number)
    result = requests.get(url)
    # print(result.status_code)
    # print(result.headers)
    c = result.content

    soup = BeautifulSoup(c, features="html.parser")
    rows = soup.find('table', {'class': 'grid'}).find_all('tr') 
    # looking at the first row
    # the address is in the second column and the sale is the fourth entry
    
    
    # grab the table column titles from html table
    pd_columns = get_columns(rows,[1,3])
    pd_columns = pd_columns[0][0],pd_columns[1][0].strip('- '),pd_columns[1][2]
    # print(pd_columns)

    # get all of the data
    dates = [
        ['1986-06-01','1987-06-01'],
        ['1987-06-01','1988-06-01'],
        ['1988-06-01','1989-06-01'],
        ['1989-06-01','1990-06-01'],

        ['1990-06-01','1991-06-01'],
        ['1991-06-01','1992-06-01'],
        ['1992-06-01','1993-06-01'],
        ['1993-06-01','1994-06-01'],
        ['1994-06-01','1995-06-01'],
        ['1995-06-01','1996-06-01'],
        ['1996-06-01','1997-06-01'],
        ['1997-06-01','1998-06-01'],
        ['1998-06-01','1999-06-01'],
        ['1999-06-01','2000-06-01'],

        ['2000-06-01','2001-06-01'],
        ['2001-06-01','2002-06-01'],
        ['2002-06-01','2003-06-01'],
        ['2003-06-01','2004-06-01'],
        ['2004-06-01','2005-06-01'],
        ['2005-06-01','2006-06-01'],
        ['2006-06-01','2007-06-01'],
        ['2007-06-01','2008-06-01'],
        ['2008-06-01','2009-06-01'],
        ['2009-06-01','2010-06-01'],

        ['2010-06-01','2011-06-01'],
        ['2011-06-01','2012-06-01'],
        ['2012-06-01','2013-06-01'],
        ['2013-06-01','2014-06-01'],
        ['2014-06-01','2015-06-01'],
        ['2015-06-01','2016-06-01'],
        ['2016-06-01','2017-06-01'],
        ['2017-06-01','2018-06-01'],
        ['2018-06-01','2019-06-01']
    ]

    
    
    # write all the data to a CSV file
    with open('property_sale.csv', mode='w',newline='') as csv_file:    
        writer = csv.writer(csv_file)
        writer.writerow(pd_columns)
        for start,end in dates:
            pd_rows = get_all_data(start,end)
            writer.writerows(pd_rows)





def get_all_data(start_date=r'2017-06-01',end_date=r'2018-06-01'):
    pages = 1
    page_number = 1
    pd_rows = []

    while page_number <= pages:
        url = r'http://www.buffalo.oarsystem.com/assessment/results.asp?swis=140200&rptname=rpt&page={p}&cnty=&urlparm=swis=140200&cnty=&tbox=&tbox=&startdate={s}&enddate={e}&lwrsaleprice=&uprsaleprice=&lwrasmt=&uprasmt=&oname1=&lwryrbuilt=&upryrbuilt=&lwrsqft=&uprsqft=&lwrbdrms=&uprbdrms=&lwrbaths=&uprbaths=&lwrfrplcs=&uprfrplcs=&searchtype=Sales&nghdcode=&prop_class=&sch_code=&hstyle=&waterfr_type=&rswis=&overall_desire=&stname='.format(s=start_date,e=end_date,p=page_number)

        # get html of the page
        result = requests.get(url)
        c = result.content
        soup = BeautifulSoup(c, features="html.parser")

        if int(page_number == 1):
            # get the number of pages 
            pages = soup.find('table', {'width': '30%'}).find('strong').contents[0]
            pages = int(pages.split(' of ')[1])
            # print(pages)

        # get the rows of the tables and add to output data
        rows = soup.find('table', {'class': 'grid'}).find_all('tr')
        
        for row in rows[1:]:
            col = row.find_all('td')
            address = col[1].find('span').contents[0]
            price,date = col[3].contents[0].split(' - ')
            pd_rows.append([address,price,date])
        page_number += 1
    # print(page_number)
    return pd_rows

def get_columns(some_soup_table,col_numbers):
    output = []
    for i in col_numbers:
        output.append(some_soup_table[0].find_all('td')[i].contents)
    return output



main()