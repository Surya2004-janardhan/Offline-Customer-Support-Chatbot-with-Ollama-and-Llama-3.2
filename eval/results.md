# Evaluation Results

## Grading Rubric
- **Relevance (1-5):** Does the response address the customer's specific query?
- **Coherence (1-5):** Is the response logical and easy to understand?
- **Helpfulness (1-5):** Does the response provide actionable information or a clear path forward?

| Query # | Customer Query | Prompting Method | Response | Relevance (1-5) | Coherence (1-5) | Helpfulness (1-5) |
|---------|----------------|------------------|----------|-----------------|-----------------|-------------------|
| 1 | How do I track the shipping status of my recent order? | Zero-Shot | You can track your order on our website. | 3 | 4 | 3 |
| 1 | How do I track the shipping status of my recent order? | One-Shot | To track your order, visit https://example.com/track and enter your Order ID. You will receive real-time updates from our courier partners. | | | |
| 2 | My discount code is not working at checkout. Can you help? | Zero-Shot | Please check if the code is expired. | 3 | 4 | 3 |
| 2 | My discount code is not working at checkout. Can you help? | One-Shot | I'm sorry your code isn't working. Please ensure the items in your cart meet the minimum requirements for the 'SAVE20' code. If the issue persists, contact our support team. | | | |
| 3 | What is your return policy for international orders? | Zero-Shot | We accept returns within 30 days. | 3 | 4 | 3 |
| 3 | What is your return policy for international orders? | One-Shot | International orders can be returned within 45 days. Please note that return shipping costs are the responsibility of the customer unless the item is defective. | | | |
| 4 | I received the wrong item in my package. How do I exchange it? | Zero-Shot | Contact support to exchange items. | 3 | 4 | 3 |
| 4 | I received the wrong item in my package. How do I exchange it? | One-Shot | We apologize for the error. To initiate an exchange for the correct item, please visit our Returns Portal and select 'Wrong Item Received'. We will provide a pre-paid shipping label. | | | |
| 5 | Can you help me reset my account password? | Zero-Shot | Click 'Forgot Password' on the login page. | 3 | 4 | 3 |
| 5 | Can you help me reset my account password? | One-Shot | To reset your password, visit the login page and click 'Forgot Password'. You will receive an email with a secure link to create a new password. For security, these links expire after 24 hours. | | | |
| 6 | Is this product available in a size medium? | Zero-Shot | Check the product page for availability. | 3 | 4 | 3 |
| 6 | Is this product available in a size medium? | One-Shot | Currently, 'Product X' is in stock in size Medium. You can select the size on the product page and add it to your cart. Hurry, as stock is limited! | | | |
| 7 | My credit card was charged twice for the same order. | Zero-Shot | Contact your bank or our support team. | 3 | 4 | 3 |
| 7 | My credit card was charged twice for the same order. | One-Shot | I apologize for the double charge. This sometimes happens if the page is refreshed during checkout. Please provide your order ID, and we will initiate a refund for the duplicate transaction immediately. | | | |
| 8 | When will my backordered item finally ship? | Zero-Shot | Backordered items ship when available. | 3 | 4 | 3 |
| 8 | When will my backordered item finally ship? | One-Shot | Your backordered item is scheduled to ship by next Friday. We will send you a confirmation email with a tracking number once it has been dispatched from our warehouse. | | | |
| 9 | I need to change the shipping address on an order I just placed. | Zero-Shot | You can edit your address in your account. | 3 | 4 | 3 |
| 9 | I need to change the shipping address on an order I just placed. | One-Shot | If your order has not yet been processed (usually within 2 hours), you can update the shipping address in your 'Order History' page. Otherwise, please contact support immediately. | | | |
| 10 | Do you offer price matching if an item goes on sale after I buy it? | Zero-Shot | We do not typically offer price matching. | 3 | 4 | 3 |
| 10 | Do you offer price matching if an item goes on sale after I buy it? | One-Shot | We offer a 14-day price protection policy. If an item you purchased goes on sale within 14 days, contact us with your order ID, and we will refund the difference as store credit. | | | |
| 11 | Can you explain how your reward points system works? | Zero-Shot | Earn points for every dollar spent. | 3 | 4 | 3 |
| 11 | Can you explain how your reward points system works? | One-Shot | Our Rewards Program grants 5 points for every $1 spent. Points can be redeemed for discounts on future orders: 500 points = $5 off. Check your balance in the 'Rewards' tab. | | | |
| 12 | Why was my order canceled without any notification? | Zero-Shot | Orders may be canceled for various reasons. | 3 | 4 | 3 |
| 12 | Why was my order canceled without any notification? | One-Shot | Orders may be canceled if items are out of stock or if payment verification fails. You should have received an automated email with the specific reason; please check your spam folder. | | | |
| 13 | How can I delete my account and remove my personal data? | Zero-Shot | You can delete your account in settings. | 3 | 4 | 3 |
| 13 | How can I delete my account and remove my personal data? | One-Shot | To permanently delete your account and associated data, please navigate to 'Account Settings' > 'Privacy' > 'Delete Account'. This action is irreversible and will remove all reward points. | | | |
| 14 | I received a defective product, how can I get a replacement? | Zero-Shot | Send us a photo of the defect for a replacement. | 3 | 4 | 3 |
| 14 | I received a defective product, how can I get a replacement? | One-Shot | We are sorry about the defect. Please email a photo of the item and your order number to replacement@example.com, and we will ship a new one to you at no additional cost. | | | |
| 15 | Is it possible to track the exact location of the delivery truck? | Zero-Shot | Live tracking is available on the courier's site. | 3 | 4 | 3 |
| 15 | Is it possible to track the exact location of the delivery truck? | One-Shot | Yes, once your order is out for delivery, you can use the 'Live Track' feature in our app to see the delivery vehicle's location in real-time on a map. | | | |
| 16 | Can I use two different promo codes on the same checkout? | Zero-Shot | Usually only one code per order is allowed. | 3 | 4 | 3 |
| 16 | Can I use two different promo codes on the same checkout? | One-Shot | Our system only permits one promotional code per transaction. However, you can use a gift card in combination with a promo code. Select 'Apply Gift Card' at checkout. | | | |
| 17 | Which payment methods do you accept for international shipping? | Zero-Shot | We accept major credit cards and PayPal. | 3 | 4 | 3 |
| 17 | Which payment methods do you accept for international shipping? | One-Shot | For international orders, we accept Visa, Mastercard, American Express, and PayPal. Some regions also support local payment methods like Klarna or iDEAL. | | | |
| 18 | How long does it typically take for a refund to process to my bank? | Zero-Shot | Refunds take 5-7 business days. | 3 | 4 | 3 |
| 18 | How long does it typically take for a refund to process to my bank? | One-Shot | Once we process a refund, it typically takes 5-10 business days to appear on your bank statement, depending on your financial institution's processing times. | | | |
| 19 | Can I change the email address associated with my account? | Zero-Shot | Yes, you can update your email in settings. | 3 | 4 | 3 |
| 19 | Can I change the email address associated with my account? | One-Shot | You can change your account email address by visiting 'Profile Settings'. You will need to verify the new email address before the change becomes final for security purposes. | | | |
| 20 | Do you offer gift wrapping services for online orders? | Zero-Shot | Gift wrapping is available at checkout. | 3 | 4 | 3 |
| 20 | Do you offer gift wrapping services for online orders? | One-Shot | Yes, we offer premium gift wrapping for $4.99. You can select this option and add a personalized message in the 'Gift Options' section during the checkout process. | | | |
