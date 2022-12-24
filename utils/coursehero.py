import requests
import time
from bs4 import BeautifulSoup

def unlockes_remaining(cookie):
    headers = {
    'authority': 'www.coursehero.com',
    'accept': '*/*',
    'accept-language': 'en-US,en-IN;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'cookie': cookie,
    'origin': 'https://www.coursehero.com',
    # 'referer': 'https://www.coursehero.com/file/55837869/ATLAS-ENGLISH-302-IMPORTANT-QUESTIONS-LESSON-1-10pdf/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }
    try:
        response = requests.get(
        'https://www.coursehero.com/api/v1/users/details/', headers=headers)
        unlockes_remaining = response.json()['unlocks_remaining']
        return unlockes_remaining
    except:
        return False

def check_unlock(doc_id, cookie):
    headers = {
    'authority': 'www.coursehero.com',
    'accept': '*/*',
    'accept-language': 'en-US,en-IN;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'cookie': cookie,
    'origin': 'https://www.coursehero.com',
    # 'referer': 'https://www.coursehero.com/file/'+str(doc_id)+'/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }
    try:
        response = requests.get(
            f'https://www.coursehero.com/api/v1/documents/download/{doc_id}/',  headers=headers)
        if response.status_code == 200:
            with open('Answer.pdf', 'wb') as f:
                f.write(response.content)
                f.close()
            return True
        else:
            return False
    except:
        return False

def unlock_document(doc_id,link, cookie):
    headers = {
    'authority': 'www.coursehero.com',
    'accept': '*/*',
    'accept-language': 'en-US,en-IN;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'cookie': cookie,
    'origin': 'https://www.coursehero.com',
    # 'referer': 'https://www.coursehero.com/file/'+str(doc_id)+'/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }
    try:
        json_data = {
            'dbFilename': doc_id,
        }

        response = requests.post('https://www.coursehero.com/api/v1/unlock-doc-action/',
                                 headers=headers, json=json_data)
        time.sleep(1)
        rs1 = requests.get(f'https://www.coursehero.com/unlock-document/{doc_id}{link}',
                         headers=headers)

        response = requests.get(
            f'https://www.coursehero.com/api/v1/documents/download/{doc_id}/',  headers=headers)
        if response.status_code == 404:
            return False
        with open('Answer.pdf', 'wb') as f:
            f.write(response.content)
            f.close()
        return True
    except:
        return False


def unlock_answer(link,cookies):
    headers = {
    'authority': 'www.coursehero.com',
    'accept': '*/*',
    'accept-language': 'en-US,en-IN;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'cookie': cookies,
    'origin': 'https://www.coursehero.com',
    # 'referer': 'https://www.coursehero.com/file/'+str(doc_id)+'/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }
    res = requests.get(link,headers=headers)
    try:
        soup = BeautifulSoup(res.content,'html.parser')
        check = soup.find('div',{'class':'no-answer answer-box'})
        if check:
            return 'NO ANSWER'
        unlock_check = soup.find('div',{'class': 'best-answer answer-box'})
        # print(unlock_check)
        unlock_button = soup.find('a',{'data-cha-target-name':'unlock_answer_btn'})
        # print(unlock_button)
        if unlock_check and unlock_button:
            try:
                print("checking")
                p = link.split('/')
                doc_ids = str(p[5]).split('-')
                unlock_id = doc_ids[0]
                print(unlock_id)
                req = requests.get(f'https://www.coursehero.com/unlock-question/{unlock_id}/',headers=headers)
                print(req.status_code)
                if req.status_code == 200:
                    res = requests.get(link,headers=headers)
                    soup = BeautifulSoup(res.content,'html.parser')
                    doc_id = soup.find('section', {'id': 'answer-content'})
                    rating = soup.find('div',{'class':'helpful-rating'})
                    rating_html = """
                    <div class="helpful-rating" style="background-color: darkgrey; color: black">
                    {}
                    </div>
                    """.format(rating)
                    with open("Answer.html",'w') as f:
                        f.write(str(doc_id))
                        f.write(rating_html)
                        f.close()
                    return True
                else:
                    return 'NOT UNLOCKED'
            except:
                return 'NOT UNLOCKED'
        doc_id = soup.find('section', {'id': 'answer-content'})
        rating = soup.find('div',{'class':'helpful-rating'})
        rating_html = """
        <div class="helpful-rating" style="background-color: darkgrey; color: black">
        {}
        </div>
        """.format(rating)
        with open("Answer.html",'w') as f:
            f.write(str(doc_id))
            f.write(rating_html)
            f.close()
        return True
    except:
        return False