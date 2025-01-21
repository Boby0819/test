from playwright.sync_api import sync_playwright
import requests 
with sync_playwright() as p:
    # 启动浏览器
    browser = p.chromium.launch(headless=False,slow_mo=1000)
    page = browser.new_page()
    
    sp_url = "https://www.xiaohongshu.com/explore/678e9d95000000001902e1eb?xsec_token=AB-Sjrnp9x766wXZ07kWq6JGjkaEla_FeU1h0tJOYW-xo=&xsec_source=pc_feed"
    # 打开目标页面
 
    page.goto(sp_url)
    page.wait_for_timeout(5000)
    try:
        pl = page.locator('#app > div:nth-child(1) > div > div.login-container > div.icon-btn-wrapper.close-button > svg')
        print('......',pl)
        if pl is not None:
            pl.click(timeout = 5000)
        # 查找<meta>元素并获取其内容
        meta_tag = page.locator('meta[name="og:video"]')
        url = meta_tag.get_attribute('content')

        # 打印获取的内容
        print('url====',url)
        res = requests.get(url,stream=True)
        with open('test2.mp4','wb') as video_file:
            for chunk in res.iter_content(chunk_size=1024):
                if chunk:
                    video_file.write(chunk)
        print('vide save success')

    except Exception as e:
        print('---------',e)
    finally:
        print('end.....')
        browser.close()

    
    # 关闭浏览器
    # browser.close()