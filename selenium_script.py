from selenium import webdriver
from selenium.webdriver.common.by import By



def scrape_website(url,target_img_url):
    # Initialize Selenium WebDriver (e.g., Chrome)
    driver = webdriver.Chrome()

    try:
        # Navigate to the URL
                driver.get(url)
              

              
                    # Scroll down until an <img> tag with specific URL is found
                scroll_height = driver.execute_script("return document.body.scrollHeight")
                while True:
                    # Scroll down to the bottom
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    
                    # Wait for some time for the content to load
                    # You might need to adjust the wait time based on your website
                    driver.implicitly_wait(2)
                    
                    # Find all img tags
                    imgs = driver.find_elements(By.TAG_NAME, 'img')
                    
                    # Check if any img tag has the target URL
                    for img in imgs:
                        if img.get_attribute("src") == target_img_url:
                            # Find the closest <a> tag to the image
                            closest_a_tag = img.find_element(By.XPATH, "./ancestor::a")     
         
                            adurl="https://adstransparency.google.com/"+closest_a_tag.get_attribute("href")    
                            break
                    
                    # Check if we reached the bottom of the page
                    new_scroll_height = driver.execute_script("return document.body.scrollHeight")
                    if new_scroll_height == scroll_height:
                        print("Reached the bottom of the page.")
                        break
                    scroll_height = new_scroll_height

                # Close the WebDriver
               

                    # Perform scraping logic after all content is loaded

                    # Close the WebDriver
                driver.quit()
                    #return scrapped data as html string
                return adurl
    except Exception as e:
                    print("An error occurred:", str(e))
                    driver.quit()
                    return None

