import requests

url = "https://istituzionale.bper.it/media-relations/comunicati-stampa?p_p_id=com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet_INSTANCE_sXZg7Pci0XFK&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet_INSTANCE_sXZg7Pci0XFK_cur=1&_com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet_INSTANCE_sXZg7Pci0XFK_delta=10"

payload={}
headers = {
  'Connection': 'keep-alive',
  'Pragma': 'no-cache',
  'Cache-Control': 'no-cache',
  'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
  'X-Requested-With': 'XMLHttpRequest',
  'X-PJAX': 'true',
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
  'Accept': '*/*',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://istituzionale.bper.it/media-relations/comunicati-stampa?p_r_p_categoryId=override_1063089080',
  'Accept-Language': 'en-US,en;q=0.9,bg;q=0.8',
  'Cookie': 'ajs_group_id=null; ajs_user_id=null; _gcl_au=1.1.1739008975.1612439674; _ga=GA1.2.703803489.1612439674; _fbp=fb.1.1612439674017.1789361377; 05387-PRIVACY_READ=true; LPVID=cxY2I5MmI1ZTI3YjBmOTk0; COOKIE_SUPPORT=true; 05387-IST-PRIVACY_READ=true; 05387-IST-ANALYTICS_ACCEPTED=true; cookiesession1=678A3E0D901234ABCDEFGHIJLNPR72CD; GUEST_LANGUAGE_ID=it_IT; LXpers=HP; pers_form_categoria=; pers_form_prodotto=; _uetsid=281fe8f0872211eba2c617f9657e831e; _uetvid=5436dd107cef11eb8c51199c465c136d; _gid=GA1.2.1787590378.1615986634; LPSID-37544564=sraUAWYhRK6ujXWiXmj9qQ; ANONYMOUS_USER_ID=1226678298; JSESSIONID=5750FA8D74DF5105BCE970BE48E4D44B.liferayprod3; last_3_page_id=["istituzionale:Homepage:Media Relations","<font style="vertical-align: inherit; persist_page_id=istituzionale:Homepage:Media Relations:Comunicati stampa; landing_page_id=istituzionale:Homepage:Media Relations:Comunicati stampa; LFR_SESSION_STATE_20120=1616051525603; utag_main=v_id:01776ce4d9bb000ddc95ac3df3e003072001d06a00bd0$_sn:5$_ss:0$_st:1616053325784$ses_id:1616050543392%3Bexp-session$_pn:10%3Bexp-session$_prevpage:istituzionale%3AHomepage%3AMedia%20Relations%3AComunicati%20stampa%3Bexp-1616055125790; _gat_global=1; _gat_sitiistituzionali=1'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
