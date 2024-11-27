# Selenium-Pytest_framework
My simple framework in PyTest currently includes logging into the system, creating a user, and logging out. The next steps are implementing order creation, navigating through the website, and managing interactions between windows.

Automated Testing on Magento Testing Site

About the Project

The test site used for this project is: https://magento.softwaretestingboard.com, which is specifically designed for testing automation purposes. However, as expected from a testing environment, the site contains several bugs and inconsistencies.



===================================================
Current Status (as of November 27, 2024) - commit 1
===================================================
	•	I have implemented a full end-to-end test for placing an order, covering the entire workflow from product selection to checkout.
	•	Unfortunately, the test currently lacks comprehensive assert functions to verify all expected results. Most assertions are limited to checking links and the pages being opened. It should ideally also validate the discount code amounts and final totals.
	•	Despite these gaps, the test is fully functional and completes the end-to-end process successfully.

Challenges and Learning Opportunities

	•	This is my first framework in pytest, and while functional, there is still much to improve and learn.
	•	Issues encountered include:
	•	Disappearing buttons: Buttons sometimes change their location or vanish, leading to difficulties in identifying elements.
	•	XPath issues: Dynamic elements with inconsistent positions often render predefined XPath ineffective.
	•	Non-unique IDs or class names: Elements lack unique identifiers, making them harder to locate reliably.
	•	Page errors: The site occasionally displays unexpected errors, further complicating the testing process.

Next Steps

In future iterations, I plan to:
	1.	Enhance Assertions:
	•	Add more robust checks for critical data, such as verifying discount amounts and total prices.
	2.	Handle Dynamic Elements:
	•	Implement advanced strategies for managing dynamic elements, such as buttons appearing in random locations.
	3.	Incorporate Advanced Features:
	•	Include handling of pop-ups, frames, and dynamic content.
	4.	Build a More Advanced Framework:
	•	Create a framework with additional features like data comparison, better error handling, and reusable modules.

Closing Note

This project is a starting point in my journey toward mastering test automation frameworks. There’s still much to refine and expand, but it represents my first step into end-to-end automated testing. Thank you for visiting this repository, and I look forward to improving further!



===================================================
Current Status (as of November 27, 2024) - commit 2
===================================================

Update: Debug File

	•	A luma debug file has been added to the tests directory.
	•	This file is specifically used for debugging pytest issues during the test runs.
	•	It contains logs and information to help identify errors or unexpected behavior in the testing process.







 
