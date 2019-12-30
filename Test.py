import Browser
import xlwt

main_url = 'https://www.xiaomiyoupin.com'
driver = Browser.Browser.get_browser()
htmls = []

class Test():
    def download_all_htmls(urls, input_url):
        driver.implicitly_wait(5)
        driver.get(input_url)
        pages_code = driver.find_elements_by_xpath("//ul[@class='nav-list']/li/span/a")

        for page_code in pages_code:
            code = page_code.get_attribute('data-src')
            url = input_url + code
            print("html:", url)
            urls.append(url)
        return urls

    def get_texts(input_url):
        texts = []
        for html in htmls:

            print(html)
            driver.get(html)
            text_pages = driver.find_elements_by_xpath("//p[@class='pro-info']")
            for text_page in text_pages:
                print(text_page.text)
                texts.append(text_page.text)

        worksheet = xlwt.Workbook()
        sheet = worksheet.add_sheet('sheet 1')
        print("write_in_xls")
        for index, item in enumerate(texts):
            sheet.write(index, 0, item)
        worksheet.save('goods.xls')

    urls = download_all_htmls(htmls, main_url)
    print(htmls)
    texts = get_texts(main_url)
