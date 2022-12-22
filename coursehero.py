# import requests

# cookies = {
#     'ch-dg-1': 'fxsm1keot4ur',
#     'PHPSESSID': '215b865f-5d47-49e0-af72-d385e4fcd45c',
#     'root_session_id': '215b865f-5d47-49e0-af72-d385e4fcd45c',
#     'device_view': 'full',
#     'nlbi_987752': 'zSTfYey7x1BXLjFS5Tz1lQAAAAB52FDnT4vcDlNShhozoE2F',
#     'visid_incap_987752': 'lJTQjTLvQk62Y1QzLdZwZ9XTo2MAAAAAQUIPAAAAAACZoHl6sKE9sR/RM6IwZp3x',
#     'incap_ses_9196_987752': '7BpDJk7yi2Mfkj/DUsGef9XTo2MAAAAADVGJYxAlO4WppnUKsQExVw==',
#     'nlbi_987752_2147483392': 'QIWeYC9b3WaDlxn75Tz1lQAAAADgavkdsW/eG9VVnAp+2uDu',
#     'incap_ses_712_987752': '4/GcAXOUhh7lFZny4ZzhCdrTo2MAAAAAQzhdpmnhonzlMsh1e6AM7A==',
#     '_ga_HR7CRKGJMD': 'GS1.1.1671680986.1.1.1671682063.0.0.0',
#     '_ga': 'GA1.2.1179630040.1671680987',
#     '_gcl_au': '1.1.1787544004.1671680987',
#     'incap_ses_707_987752': '49+LT0+JnBmTFvZakMXPCdrTo2MAAAAAD3qaQUGscRkZyoJGia3wDg==',
#     'has_called_TBM': '1',
#     'reese84': '3:gqXS9qKPU3vHjmWDtl5YAA==:Tw+vuWgUsqt/AC1RKcmhaS+R7xw/4vPndteyP/QDuSxcIL45Nd6uBoAq5bw5gOXsJc6nWpvnqiHu3rCHMYWI2Ugaj2dxZMBsDTA9Uo+mYY3xoGbyB2b3HoMIwPhvZmHUejJFqFTmTrZla5K4YZXsYxs7ScFxj2pyg1Dfy4sx2sPMiRm82HbNCkUPufbwuFWS54xUO/Usr1iQW5caoz8oQk0Rp6OdxIvape/KCJNsV3ekYQfj9lyiHqf+q/x4D2Jy8buWRMzUHKIyxjbBXMV90MM21mR7df3HJ6nT4eM3iSeTq1hixT46DeamAT77mG1C22eydCQfi6VVD3hJohMAY6mos6se+Nt6ZrKZXmnbug8cFBaCmL4c+lgDXiw6lGNGu9MfwhszgYj5TGaFTzRrEHzo09C66TrhlC+GbLh0F3bLjz4kWkN90NVfiuxpUFMSvYZI8arqDrWyZqOfizZ3zjvl5zSS2FmaGCTIL48Ja5oWvHEtQJDAQNwAyHfbiyyujnq2B1EBBqyQkWTHuard9g==:osAe2hUAHHLXkysGG3cRdNIlqtQp6FeE5VzyNQ0NCwY=',
#     'ln_or': 'eyIxMjg2MDkyIjoiZCJ9',
#     '_gid': 'GA1.2.1601690982.1671680988',
#     'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Dec+22+2022+09%3A37%3A45+GMT%2B0530+(India+Standard+Time)&version=202210.1.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0004%3A1%2CC0003%3A1%2CC0002%3A1&geolocation=IN%3BAP&AwaitingReconsent=false',
#     'OptanonAlertBoxClosed': '2022-12-22T04:07:45.173Z',
#     'QSI_CT': '{"gtm.init_consent":12,"gtm.init":12,"gtm.js":12,"gtm.dom":12,"OneTrustLoaded":17,"OptanonLoaded":17,"OneTrustGroupsUpdated":13,"gtm.load":12,"gtm.scrollDepth":32,"login-success":1,"gtm.linkClick":9,"gtm.historyChange-v2":4,"page_view":4,"scroll":6,"unlock_content":1}',
#     'G_ENABLED_IDPS': 'google',
#     'userID': '100000859551968',
#     'ch_logged_in': '1',
#     'supportEmail': 'bba31913%40xcoxc.com',
#     'has_successfully_logged_in_the_past': '1',
#     'remember_me': '100000859551968%7C%7CMsakAPAIbYiAmV1jeBCdnfT7Hr7SACfo',
#     # 'recently_viewed_docs': '11712160%2C',
#     'has_seen_mcq': 'yes',
#     'has_closed_cro1657_privacy_banner': 'true',
# }

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#     'Accept-Language': 'en-US,en;q=0.5',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     'Referer': 'https://www.coursehero.com/u/file/11712160/Sample-questions/',
#     'Connection': 'keep-alive',
#     # 'Cookie': 'ch-dg-1=fxsm1keot4ur; PHPSESSID=215b865f-5d47-49e0-af72-d385e4fcd45c; root_session_id=215b865f-5d47-49e0-af72-d385e4fcd45c; device_view=full; nlbi_987752=zSTfYey7x1BXLjFS5Tz1lQAAAAB52FDnT4vcDlNShhozoE2F; visid_incap_987752=lJTQjTLvQk62Y1QzLdZwZ9XTo2MAAAAAQUIPAAAAAACZoHl6sKE9sR/RM6IwZp3x; incap_ses_9196_987752=7BpDJk7yi2Mfkj/DUsGef9XTo2MAAAAADVGJYxAlO4WppnUKsQExVw==; nlbi_987752_2147483392=QIWeYC9b3WaDlxn75Tz1lQAAAADgavkdsW/eG9VVnAp+2uDu; incap_ses_712_987752=4/GcAXOUhh7lFZny4ZzhCdrTo2MAAAAAQzhdpmnhonzlMsh1e6AM7A==; _ga_HR7CRKGJMD=GS1.1.1671680986.1.1.1671682063.0.0.0; _ga=GA1.2.1179630040.1671680987; _gcl_au=1.1.1787544004.1671680987; incap_ses_707_987752=49+LT0+JnBmTFvZakMXPCdrTo2MAAAAAD3qaQUGscRkZyoJGia3wDg==; has_called_TBM=1; reese84=3:gqXS9qKPU3vHjmWDtl5YAA==:Tw+vuWgUsqt/AC1RKcmhaS+R7xw/4vPndteyP/QDuSxcIL45Nd6uBoAq5bw5gOXsJc6nWpvnqiHu3rCHMYWI2Ugaj2dxZMBsDTA9Uo+mYY3xoGbyB2b3HoMIwPhvZmHUejJFqFTmTrZla5K4YZXsYxs7ScFxj2pyg1Dfy4sx2sPMiRm82HbNCkUPufbwuFWS54xUO/Usr1iQW5caoz8oQk0Rp6OdxIvape/KCJNsV3ekYQfj9lyiHqf+q/x4D2Jy8buWRMzUHKIyxjbBXMV90MM21mR7df3HJ6nT4eM3iSeTq1hixT46DeamAT77mG1C22eydCQfi6VVD3hJohMAY6mos6se+Nt6ZrKZXmnbug8cFBaCmL4c+lgDXiw6lGNGu9MfwhszgYj5TGaFTzRrEHzo09C66TrhlC+GbLh0F3bLjz4kWkN90NVfiuxpUFMSvYZI8arqDrWyZqOfizZ3zjvl5zSS2FmaGCTIL48Ja5oWvHEtQJDAQNwAyHfbiyyujnq2B1EBBqyQkWTHuard9g==:osAe2hUAHHLXkysGG3cRdNIlqtQp6FeE5VzyNQ0NCwY=; ln_or=eyIxMjg2MDkyIjoiZCJ9; _gid=GA1.2.1601690982.1671680988; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Dec+22+2022+09%3A37%3A45+GMT%2B0530+(India+Standard+Time)&version=202210.1.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0004%3A1%2CC0003%3A1%2CC0002%3A1&geolocation=IN%3BAP&AwaitingReconsent=false; OptanonAlertBoxClosed=2022-12-22T04:07:45.173Z; QSI_CT={"gtm.init_consent":12,"gtm.init":12,"gtm.js":12,"gtm.dom":12,"OneTrustLoaded":17,"OptanonLoaded":17,"OneTrustGroupsUpdated":13,"gtm.load":12,"gtm.scrollDepth":32,"login-success":1,"gtm.linkClick":9,"gtm.historyChange-v2":4,"page_view":4,"scroll":6,"unlock_content":1}; G_ENABLED_IDPS=google; userID=100000859551968; ch_logged_in=1; supportEmail=bba31913%40xcoxc.com; has_successfully_logged_in_the_past=1; remember_me=100000859551968%7C%7CMsakAPAIbYiAmV1jeBCdnfT7Hr7SACfo; recently_viewed_docs=11712160%2C; has_seen_mcq=yes; has_closed_cro1657_privacy_banner=true',
#     'Upgrade-Insecure-Requests': '1',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     'Sec-Fetch-User': '?1',
#     # Requests doesn't support trailers
#     # 'TE': 'trailers',
# }

# response = requests.get(
#     'https://www.coursehero.com/api/v1/documents/download/55837869/', cookies=cookies, headers=headers)
# print(response.status_code)


import requests
import time
doc_id = 135739736

cookies = {
    'root_session_id': '925c07f4-0ead-4a1d-9532-df8b49b7da74',
    'visid_incap_987752': '3Udb4wM1QoitJYCuPXJWnVzSmmIAAAAAQUIPAAAAAAAXdNdHdMFNMQOBZ15YGmqi',
    'G_ENABLED_IDPS': 'google',
    'incap_ses_712_987752': 'M8bCNUDYxFzSzaHy4ZzhCbngo2MAAAAAZKmJhrze0gM+bagNqtDHIQ==',
    'PHPSESSID': '7f99617c-d52d-4f4d-875f-19d19f26b511',
    'nlbi_987752': 'SxObEYdtmVsKsRvA5Tz1lQAAAADsBpHgapB3M6qpzKXW5CaO',
    'incap_ses_704_987752': 'V0fONHftgVz84Ny+iBzFCbrgo2MAAAAApYmHScda2euF/Auhpbt+Bg==',
    'ch-dg-1': '316wzwnw2xlrf',
    'device_view': 'full',
    'userID': '100000859551968',
    'ch_logged_in': '1',
    'supportEmail': 'bba31913%40xcoxc.com',
    'has_successfully_logged_in_the_past': '1',
    'remember_me': '100000859551968%7C%7CNwmaIISZAdrX4ERVPXwZmobs3LxsbNof',
    'has_called_TBM': '1',
    'recently_viewed_docs': '55837869%2C',
    'has_seen_mcq': 'yes',
    'OptanonAlertBoxClosed': '2022-12-22T05:01:48.902Z',
    'OptanonConsent': 'isIABGlobal=false&datestamp=Thu+Dec+22+2022+10%3A31%3A49+GMT%2B0530+(India+Standard+Time)&version=202210.1.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0004%3A1%2CC0003%3A1%2CC0002%3A1&AwaitingReconsent=false&geolocation=IN%3BTG',
    'nlbi_987752_2147483392': 'z5CFXHVEPh8bVX5Q5Tz1lQAAAAC6gxjIk11QsEu/0xdBCzeI',
    'reese84': '3:kYcXMjtF2wWGALOGEZCyKw==:Yucd4ogUzFClcflFvO+f2nL+BIv2RT6Ph+W0iYQ9LWIShHkzI+92ZGmmijDX1hPd8QD18IgpMtcubEY6mFVap/Qn1E8vEtYaUmzKBZNiOA4wAD5lUtAZWY7leLH0/IJuwdnPI3W8RiR3tHQHUME5KZSBX6EqensYHJznM9HlojFc4j2x88HeadXlCdTUfLcCEZC0tYCKwM5IlgNWnlpSeoyOGvrkaQuaR9PWavvmKCw5+rMDwODS48Y0Bnwr1PKfx8MDkfIWqlAg7yk9qyPCUbxXpmsltTBlXzTLEwz/Ty33/h76Lt0rXLmd6tGbCDRpzB/CNqfx5ZRdJWhtGAQfiC9kX054fLih9VwHCBfsgR6JJDKa6pDh4KZt154nOGVwa2RkXoXXgh2MEl5VgcWN+EC3riG3znqGvPpuSgr3T0RzPWXrPBoyeVueYYcPbPOcDWceraUwSPC0zHKXWrKLpdjhAu/1kfCM0w9QRGLyNhM=:MT5YmUp2oJdZX3vQayTvPJAH9e9x1weK4n6ifEgKybw=',
}

headers = {
    'authority': 'www.coursehero.com',
    'accept': '*/*',
    'accept-language': 'en-US,en-IN;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    # 'cookie': 'root_session_id=925c07f4-0ead-4a1d-9532-df8b49b7da74; visid_incap_987752=3Udb4wM1QoitJYCuPXJWnVzSmmIAAAAAQUIPAAAAAAAXdNdHdMFNMQOBZ15YGmqi; G_ENABLED_IDPS=google; incap_ses_712_987752=M8bCNUDYxFzSzaHy4ZzhCbngo2MAAAAAZKmJhrze0gM+bagNqtDHIQ==; PHPSESSID=7f99617c-d52d-4f4d-875f-19d19f26b511; nlbi_987752=SxObEYdtmVsKsRvA5Tz1lQAAAADsBpHgapB3M6qpzKXW5CaO; incap_ses_704_987752=V0fONHftgVz84Ny+iBzFCbrgo2MAAAAApYmHScda2euF/Auhpbt+Bg==; ch-dg-1=316wzwnw2xlrf; device_view=full; userID=100000859551968; ch_logged_in=1; supportEmail=bba31913%40xcoxc.com; has_successfully_logged_in_the_past=1; remember_me=100000859551968%7C%7CNwmaIISZAdrX4ERVPXwZmobs3LxsbNof; has_called_TBM=1; recently_viewed_docs=55837869%2C; has_seen_mcq=yes; OptanonAlertBoxClosed=2022-12-22T05:01:48.902Z; OptanonConsent=isIABGlobal=false&datestamp=Thu+Dec+22+2022+10%3A31%3A49+GMT%2B0530+(India+Standard+Time)&version=202210.1.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0004%3A1%2CC0003%3A1%2CC0002%3A1&AwaitingReconsent=false&geolocation=IN%3BTG; nlbi_987752_2147483392=z5CFXHVEPh8bVX5Q5Tz1lQAAAAC6gxjIk11QsEu/0xdBCzeI; reese84=3:kYcXMjtF2wWGALOGEZCyKw==:Yucd4ogUzFClcflFvO+f2nL+BIv2RT6Ph+W0iYQ9LWIShHkzI+92ZGmmijDX1hPd8QD18IgpMtcubEY6mFVap/Qn1E8vEtYaUmzKBZNiOA4wAD5lUtAZWY7leLH0/IJuwdnPI3W8RiR3tHQHUME5KZSBX6EqensYHJznM9HlojFc4j2x88HeadXlCdTUfLcCEZC0tYCKwM5IlgNWnlpSeoyOGvrkaQuaR9PWavvmKCw5+rMDwODS48Y0Bnwr1PKfx8MDkfIWqlAg7yk9qyPCUbxXpmsltTBlXzTLEwz/Ty33/h76Lt0rXLmd6tGbCDRpzB/CNqfx5ZRdJWhtGAQfiC9kX054fLih9VwHCBfsgR6JJDKa6pDh4KZt154nOGVwa2RkXoXXgh2MEl5VgcWN+EC3riG3znqGvPpuSgr3T0RzPWXrPBoyeVueYYcPbPOcDWceraUwSPC0zHKXWrKLpdjhAu/1kfCM0w9QRGLyNhM=:MT5YmUp2oJdZX3vQayTvPJAH9e9x1weK4n6ifEgKybw=',
    'origin': 'https://www.coursehero.com',
    'referer': 'https://www.coursehero.com/file/55837869/ATLAS-ENGLISH-302-IMPORTANT-QUESTIONS-LESSON-1-10pdf/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

response = requests.get(
    'https://www.coursehero.com/api/v1/users/details/', cookies=cookies, headers=headers)

unlockes_remaining = response.json()['unlocks_remaining']
# json_data = {
#     'dbFilename': doc_id,
# }

# response = requests.post('https://www.coursehero.com/api/v1/unlock-doc-action/',
#                          cookies=cookies, headers=headers, json=json_data)
# print(response.status_code)
# time.sleep(1)
# rs1 = requests.get('https://www.coursehero.com/unlock-document/135739736/A-Good-Man-is-Hard-to-Find-by-Flannery-OConnordocx/',
#                    cookies=cookies, headers=headers)
# print(rs1.status_code)

# response = requests.get(
#     f'https://www.coursehero.com/api/v1/documents/download/{doc_id}/', cookies=cookies, headers=headers)
# print(response.status_code)

# with open('Answer.pdf', 'wb') as f:
#     f.write(response.content)
#     f.close()
