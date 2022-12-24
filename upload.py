import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import random
import string
import hashlib

def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()


cookies = {
    'root_session_id': '925c07f4-0ead-4a1d-9532-df8b49b7da74',
    'visid_incap_987752': '3Udb4wM1QoitJYCuPXJWnVzSmmIAAAAAQUIPAAAAAAAXdNdHdMFNMQOBZ15YGmqi',
    'G_ENABLED_IDPS': 'google',
    'device_view': 'full',
    'ch_logged_in': '1',
    'has_successfully_logged_in_the_past': '1',
    'recently_viewed_docs': '76202171%2C135739736%2C55837869%2C',
    'last_viewed_question': '27434856',
    'PHPSESSID': 'ae54d571-0c4d-4edb-9b4f-e4b638851a8f',
    'remember_me': '100000859551968%7C%7CuSXYMMclXe53Hdh28QnrQ%2B7jBGen9I',
    'userID': '100000859551968',
    'nlbi_987752': 'azv1Fd/ZlnUSXlZa5Tz1lQAAAAApgBnjiQ6pBTmBjK4B8p6c',
    'incap_ses_704_987752': 'Ij5oI0S4UH5iUS7AiBzFCQ+DpmMAAAAA/46iFDxaToTCpW27sfFt2g==',
    'has_called_TBM': '1',
    'OptanonConsent': 'isIABGlobal=false&datestamp=Sat+Dec+24+2022+10%3A11%3A59+GMT%2B0530+(India+Standard+Time)&version=202210.1.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0004%3A1%2CC0003%3A1%2CC0002%3A1&AwaitingReconsent=false&geolocation=IN%3BTG',
    'OptanonAlertBoxClosed': '2022-12-24T04:41:59.365Z',
    'nlbi_987752_2147483392': '1il2AWv7lx9anGTI5Tz1lQAAAACwj2ua4lhl2Qakk/+D0Zkz',
    'incap_ses_710_987752': 'd/6oFuAUUE5M85FT923aCbSGpmMAAAAAXXz4O5c/pIK7fPIQ/VmLLw==',
    'reese84': '3:R7kLCyhzUhy4G5PgO55nUQ==:bLSGOju1b8WX7puqjEFtCucNbs4Oyj2wES72nTatEFGTGugwOP5isKjd6noE9BAnhtENPX4jE7JMTEqStyC8lViG3BuKMXsxDVmCYBitYpiEU5dgBMhktL7/W+A09kNQBtrqG0hdbaWCChDCmWTzRkBG2zPaMVioIaMW9mjSicL9UWXDggtEFU6tXRGcULQd3zgmonflZ0MrQhsF+jxxxr2otS9ZVtFsT9QpOcd5eWJlhv22loRO9Yb9SlJUBS8W7DvN99uTFOraI+fa9ElqZLjYUqNIqr2w9JmQjad9JtlnAgFSUMw2x3gnSP1gZHKB4h90vAnV2TR7ZTFMBLq08hN8Jkldh4QATXL0FROtNO8FlAMluQWaj356fhQVlrAtgniDDnZ7Nb+qZOJiMPnWod/DCnjv7lHlTwwv+i+iItkvModkKLp0yiYfW6eoMuXoQ2w7tNRr7zFNzHawVJUvnvJW9SvOb72gNEvnQarRFag=:eASTauHo9g7CfA038bjQTlRCkVdbQGOhR/bQXoPqq2A=',
    'incap_ses_708_987752': 'UG7VShQSfy1SKaqvDFPTCdGGpmMAAAAAfEJpy5wfsb2yb9fxU1BkLg==',
    'incap_ses_712_987752': 'NaSueeUhoS0EMTf04ZzhCfCGpmMAAAAA0TFclrp3UoRz5Cg7NqTkGA==',
    'incap_ses_713_987752': '8nKBH6FK4EXwH9GTfBblCQ6HpmMAAAAACqV8qydUQ9vDtAouJrg0rA==',
    'incap_ses_706_987752': 'd+9fX/0Ofz/RKkJtDzjMCS2HpmMAAAAANdSzEbNz4u5MVS7YKxbztA==',
    'ch-dg-1': '2fwkgtunudx3g',
    'incap_ses_711_987752': 'qodxVC7YR3ncoO9K6vrdCdCHpmMAAAAAncHem/YfC4Fpi1l1FzTmxg==',
    'incap_ses_715_987752': '/mjraSs7rifd8LM0dTHsCe2HpmMAAAAAnPnbvpjcYM0cM8FEAF5gBw==',
    'incap_ses_707_987752': 'oJ8tVv6VImI9zxpckMXPCfqHpmMAAAAA5G+i/eeB5TMag2XgmnshXQ==',
}

headers = {
    'authority': 'www.coursehero.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en-IN;q=0.9,en;q=0.8',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryfNXq94ANSqbDuYhe',
    # 'cookie': 'root_session_id=925c07f4-0ead-4a1d-9532-df8b49b7da74; visid_incap_987752=3Udb4wM1QoitJYCuPXJWnVzSmmIAAAAAQUIPAAAAAAAXdNdHdMFNMQOBZ15YGmqi; G_ENABLED_IDPS=google; device_view=full; ch_logged_in=1; has_successfully_logged_in_the_past=1; recently_viewed_docs=76202171%2C135739736%2C55837869%2C; last_viewed_question=27434856; PHPSESSID=ae54d571-0c4d-4edb-9b4f-e4b638851a8f; remember_me=100000859551968%7C%7CuSXYMMclXe53Hdh28QnrQ%2B7jBGen9I; userID=100000859551968; nlbi_987752=azv1Fd/ZlnUSXlZa5Tz1lQAAAAApgBnjiQ6pBTmBjK4B8p6c; incap_ses_704_987752=Ij5oI0S4UH5iUS7AiBzFCQ+DpmMAAAAA/46iFDxaToTCpW27sfFt2g==; has_called_TBM=1; OptanonConsent=isIABGlobal=false&datestamp=Sat+Dec+24+2022+10%3A11%3A59+GMT%2B0530+(India+Standard+Time)&version=202210.1.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0004%3A1%2CC0003%3A1%2CC0002%3A1&AwaitingReconsent=false&geolocation=IN%3BTG; OptanonAlertBoxClosed=2022-12-24T04:41:59.365Z; nlbi_987752_2147483392=1il2AWv7lx9anGTI5Tz1lQAAAACwj2ua4lhl2Qakk/+D0Zkz; incap_ses_710_987752=d/6oFuAUUE5M85FT923aCbSGpmMAAAAAXXz4O5c/pIK7fPIQ/VmLLw==; reese84=3:R7kLCyhzUhy4G5PgO55nUQ==:bLSGOju1b8WX7puqjEFtCucNbs4Oyj2wES72nTatEFGTGugwOP5isKjd6noE9BAnhtENPX4jE7JMTEqStyC8lViG3BuKMXsxDVmCYBitYpiEU5dgBMhktL7/W+A09kNQBtrqG0hdbaWCChDCmWTzRkBG2zPaMVioIaMW9mjSicL9UWXDggtEFU6tXRGcULQd3zgmonflZ0MrQhsF+jxxxr2otS9ZVtFsT9QpOcd5eWJlhv22loRO9Yb9SlJUBS8W7DvN99uTFOraI+fa9ElqZLjYUqNIqr2w9JmQjad9JtlnAgFSUMw2x3gnSP1gZHKB4h90vAnV2TR7ZTFMBLq08hN8Jkldh4QATXL0FROtNO8FlAMluQWaj356fhQVlrAtgniDDnZ7Nb+qZOJiMPnWod/DCnjv7lHlTwwv+i+iItkvModkKLp0yiYfW6eoMuXoQ2w7tNRr7zFNzHawVJUvnvJW9SvOb72gNEvnQarRFag=:eASTauHo9g7CfA038bjQTlRCkVdbQGOhR/bQXoPqq2A=; incap_ses_708_987752=UG7VShQSfy1SKaqvDFPTCdGGpmMAAAAAfEJpy5wfsb2yb9fxU1BkLg==; incap_ses_712_987752=NaSueeUhoS0EMTf04ZzhCfCGpmMAAAAA0TFclrp3UoRz5Cg7NqTkGA==; incap_ses_713_987752=8nKBH6FK4EXwH9GTfBblCQ6HpmMAAAAACqV8qydUQ9vDtAouJrg0rA==; incap_ses_706_987752=d+9fX/0Ofz/RKkJtDzjMCS2HpmMAAAAANdSzEbNz4u5MVS7YKxbztA==; ch-dg-1=2fwkgtunudx3g; incap_ses_711_987752=qodxVC7YR3ncoO9K6vrdCdCHpmMAAAAAncHem/YfC4Fpi1l1FzTmxg==; incap_ses_715_987752=/mjraSs7rifd8LM0dTHsCe2HpmMAAAAAnPnbvpjcYM0cM8FEAF5gBw==; incap_ses_707_987752=oJ8tVv6VImI9zxpckMXPCfqHpmMAAAAA5G+i/eeB5TMag2XgmnshXQ==',
    'origin': 'https://www.coursehero.com',
    'referer': 'https://www.coursehero.com/upload/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}


response = requests.post('https://www.coursehero.com/api/v1/documentSubmission/', cookies=cookies, headers=headers)
print(response.content)
# submission_id = response.json()['documentSubmissionId']


files = {
    'file': ('DOCMENTS/Doc_11.pdf', open('DOCMENTS/Doc_11.pdf', 'rb'), 'application/pdf'),
    'method': (None,'regular'),
    'source': (None,'Desktop'),
    'course_id': (None,'10122614'),
    'school_id': (None,'81452'),
    'is_mandatory_tagging': (None,'true'),
    'is_mandatory_tagging': (None,'true'),
    'document_submission_id': (None,str(submission_id)),
    'hash':(None, hash_file('DOCMENTS/Doc_11.pdf')),
    'upload_application_name':(None, 'flu'),
    'upload_application_version': (None,'upld_flu_legal_disclaimer_v2_0'),
}
# fields={"auth":{"id":str(random.randint(0, 999991)),"sign":randoms(32)},
#     "data":{"action":"login","login":"embrella","password":"steffano321","stayLogged":"False"}
#     }
# {"auth":'{{}:{},"sign":{}}'.format('id', random.randint(0, 999991), randoms(32)) but now it says ValueError: Single '}'

boundary = '----WebKitFormBoundary' \
                        + ''.join(random.sample(string.ascii_letters + string.digits, 16))
m = MultipartEncoder(fields=files, boundary=boundary)

print(m)

headers['content-type'] = f'multipart/form-data; boundary={boundary}'


response = requests.post('https://www.coursehero.com/api/v1/uploads/', cookies=cookies, headers=headers, data=m)
print(response.json())