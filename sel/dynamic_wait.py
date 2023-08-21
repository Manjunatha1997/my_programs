def wait_for(driver, xpath, timer=30):
    counter = 0
    found = 0
    while True:
        try:
            el = driver.find_element_by_xpath(xpath)
            found = 1
            break
        except:
            time.sleep(2)
            if counter >= timer:
                break
            counter = counter + 2
    return found
