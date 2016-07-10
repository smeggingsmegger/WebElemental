# Elemental
A helpful wrapper for Selenium

[![Build Status](https://travis-ci.org/smeggingsmegger/WebElemental.svg?branch=master)](https://travis-ci.org/smeggingsmegger/WebElemental)

Full documentation can be located here: [https://smeggingsmegger.github.io/WebElemental](https://smeggingsmegger.github.io/WebElemental)

You could use Elemental to scrape a website, automate web tasks, or anything else you could imagine. It is easy to initialize and use. It's also compatible with [BrowserStack](https://www.browserstack.com/automate/python) using the command_executor and remote_capabilities examples on that page. Please note that you will need a subscription, username, and API key to make it work.

```python
from WebElemental import Elemental

# Running headless FireFox is the default.
elemental = Elemental() # Defaults to xvfb=True, driver=FireFox
# If xvfb is not installed, it will be bypassed automatically.

# If you explicitly don't want headless operation:
elemental = Elemental(xvfb=False)

```

Once we've initialized Elemental, we still need to kick off the browser. I've made this a manual step so that it is easy to start and stop different browsers using the same Elemental instance if desired.

```python
# Start your engines...

elemental.start()

# DO SOME STUFF

elemental.stop()
```

Let's say you wanted to do some things in FireFox and then switch to Chrome. You could do it like so:

```python
elemental = Elemental()

elemental.start()

# Do things...

elemental.stop()

# Change the browser. This is accomplished by setting the property directly at present.
elemental.browser = "Chrome"

# You could also choose to run headlessly if you wanted:
elemental.xvfb = True

elemental.start()

# Do things in Chrome now.

elemental.stop()
```

The main utility of the Elemental class is its ability to shortcut many of the most common tasks that you would need to automate the interaction with a web page.

The most critical of these would be to open a webpage.

```python
elemental.go('http://someaddress.here/page.html')
```

Once we have a page open we can interact with it in various ways. The methods in this class are well-documented so fully explaining them all is outside of the scope of this guide. I strongly recommend that you look at the docstrings for all the methods and see for yourself how to interact with them.

Here is a list of available methods in Elemental with basic explanations about what they do:

### Browser control:
- start
- stop
- refresh_page
- forward
- back
- go
- current_url
- js

#### Scrolling
- scroll_browser

#### Misc
- get_page_source
- screenshot
- save_page_source

#### Waiting
- wait_for_url
- wait_for_title
- wait_for_js

#### Finding
- is_text_on_page

### Element Methods

#### Scrolling
- scroll_to_element

#### Selecting
- find_element
- find_elements
- get_element
- get_elements
- get_text
- get_value
- get_texts

#### Waiting
- wait_for
- wait_for_visible
- wait_for_invisible
- wait_for_all_invisible
- wait_for_clickable
- wait_for_selected
- wait_for_presence
- wait_for_opacity
- wait_for_text
- wait_for_text_in_value
- wait_for_value
- wait_for_ko

#### Interaction
- click
- click_all
- hover
- send_key
- clear

#### Forms
- fill
- fill_form
- set_value
- set_selectize
- set_select_by_value
- set_select_by_text

```python
print(elemental.current_url())
# outputs 'http://someaddress.here/page.html'

elemental.click('#some-button') # Clicks a button.

elemental.js('console.log("I am executing JS on the page!");')

elem = elemental.find_element('#my-id') # Returns a selenium element object

elems = elemental.find_elements('.some-class') # Returns a list of selenium element objects

form_data = {
	'#username': 'person',
	'#password': 'somepass'
}
elemental.fill(form_data) # Fills a form. Takes a dict of CSS keys and values.

elemental.screenshot('/tmp/screenshot1.png')
```

#### BrowserStack example:

```python
from WebElemental import Elemental
desired = {
	'browser': 'Edge',
	'browser_version': '13.0',
	'os': 'Windows',
	'os_version': '10',
	'resolution': '1440x900'
}
elemental = Elemental(desired_capabilities=desired,
               command_executor='http://USERNAME:API_KEY@hub.browserstack.com:80/wd/hub',
							 driver='Remote')
elemental.start()
elemental.go('http://google.com')
elemental.set_value('#lst-ib', 'WebElemental')
```

As you can see, there is almost no reason to ever interact with the selenium browser object directly. This is by design. If you ever find yourself needing to, it means that you have uncovered a need that was unanticipated by the initial design of this utility.

If you are reading this, you are a programmer so it would be nice if you made the method you require and sent a PR. The more people use and develop this framework, the better it will become.

So even though I don't recommend using it, you still have access to the selenium browser object.

```python
elemental.browser.find_elements_by_id('#some-id') # Use elemental.find_element instead.
```
----

# TestElemental

TestElemental inherits Elemental so it has all the same methods that Elemental has but it adds some additional methods that are useful for testing.

### Helpers
- goto
- wait

### Testing Asserts
- assert_element_has_class
- assert_not_found
- assert_not_visible
- assert_exists
- assert_alert_present
- assert_text_in_page
- assert_visible
- assert_text_not_in_page
- assert_url
- assert_alert_not_present
- assert_text_in_elements
- assert_text_in_element
- assert_found
- assert_element_contains_text
- assert_value_of_element
- assert_element_not_has_class
