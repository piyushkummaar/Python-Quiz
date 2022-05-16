def write_csv(data):
    '''
    repr : This funtion take the argument as the nested list to insert data into the CSV file. 
    '''
    try:
        header = ['Company', 'Street', 'City', 'St', 'ZIPCode','Verified']
        data = data
        with open('Addressverifed.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            # write the header
            writer.writerow(header)
            # write multiple rows
            writer.writerows(data)
        print("[INFO] File write successfully.")
        return True
    except:
        return False
def scrap_data():
    '''
    repr : This funtion take the argument as the html content and parse that content 
           Then vailded that address and create CSV file.
    '''
    try:
        url = "https://docs.google.com/spreadsheets/d/1H1a9eBamflt3w-4BPEk1kJYc4VgsDBWlDjkS0hV5tAY/edit#gid=0"
        res = requests.get(url)
        # making a get request for google sheet
        soup = BeautifulSoup(res.content, "html.parser")
        print("[INFO] Successfully extract the data from the google sheet.")
        # passing the html response into the beautifulsoup 
        extract_data = [ x for x in [i.text.strip() for i in soup.find_all("td")] if len(x) > 0][:-2]
        # scrape  data from the target google sheet

        new_list = []
        # new_list contains the data with the verified address status
        count = 5

        for i in range(0,int(len(extract_data)/5)):
            if count == 5:
                temp_list = extract_data[count:count+5]
                if temp_list:
                    payload = {
                    "companyName":temp_list[0],
                    "address1":temp_list[1],
                    "city":temp_list[2],
                    "state":temp_list[3],
                    "zip":temp_list[4]
                    }
                    if verify_url(payload):
                        temp_list.append("True")
                    else:
                        temp_list.append("False") 
                    new_list.append(temp_list)
            elif count > 5:
                temp_list = extract_data[count:count+5]
                if temp_list:
                    payload = {
                    "companyName":temp_list[0],
                    "address1":temp_list[1],
                    "city":temp_list[2],
                    "state":temp_list[3],
                    "zip":temp_list[4]
                    }
                    if verify_url(payload):
                        temp_list.append("True")
                    else:
                        temp_list.append("False")
                    new_list.append(temp_list)
            count = count + 5
        # writing the csv file
        write_csv(new_list)
    except Exception as e:
        return False
def verify_url(inp_data):
    '''
    repr : this function take inp_data as input dict and check submitted details is correct or not 
    '''
    try:
        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39",
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        # making an post request using the useragent to verify the input data is correct or not.
        post_res = requests.post("https://tools.usps.com/tools/app/ziplookup/zipByAddress",headers=header,data=inp_data)
        # check if address found or not
        if post_res.json().get("resultStatus") == "SUCCESS":
            # if address found
            return True
        else:
            # when address not founc
            return False
    except Exception as e:
        return False

if __name__ == "__main__":
    import requests
    from bs4 import BeautifulSoup
    import csv  

    # main function executes
    scrap_data()