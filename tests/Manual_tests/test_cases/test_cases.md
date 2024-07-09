# Test Cases

## 1. Functional Testing

### Test Case ID: TC_FT_001
- **Test Case Name**: Login with valid credentials
- **Description**: Verify that users can log in with valid credentials.
- **Pre-conditions**: User is on the login page.
- **Test Steps**:
  1. Enter valid username.
  2. Enter valid password.
  3. Click on the login button.
- **Expected Result**: User is redirected to the inventory page.

### Test Case ID: TC_FT_002
- **Test Case Name**: Login with invalid credentials
- **Description**: Verify that users cannot log in with invalid credentials.
- **Pre-conditions**: User is on the login page.
- **Test Steps**:
  1. Enter invalid username.
  2. Enter invalid password.
  3. Click on the login button.
- **Expected Result**: Error message is displayed.

### Test Case ID: TC_FT_003
- **Test Case Name**: Product search functionality
- **Description**: Verify that users can search for products.
- **Pre-conditions**: User is logged in and on the inventory page.
- **Test Steps**:
  1. Enter product name in the search bar.
  2. Click on the search button.
- **Expected Result**: Relevant products are displayed.

### Test Case ID: TC_FT_004
- **Test Case Name**: Logout functionality
- **Description**: Verify that users can logout from the application.
- **Pre-conditions**: User is logged in.
- **Test Steps**:
  1. Click on the menu button.
  2. Click on the logout link.
- **Expected Result**: User is redirected to the login page.

### Test Case ID: TC_FT_005
- **Test Case Name**: Checkout functionality
- **Description**: Verify that users can successfully place an order and navigate back to the home page.
- **Pre-conditions**: User has added items to the cart and is on the checkout page.
- **Test Steps**:
  1. Fill out checkout information.
  2. Click on the finish button.
  3. Click on the 'Back Home' button.
- **Expected Result**: 
   - "Order placed successfully!" message is displayed.
   - User is navigated back to the home page.

### Test Case ID: TC_FT_006
- **Test Case Name**: Product search and add to cart functionality
- **Description**: Verify that users can search for a product and add it to the cart.
- **Pre-conditions**: User is logged in and on the inventory page.
- **Test Steps**:
  1. Login with valid credentials.
  2. Search for a specific product.
  3. Add the product to the cart.
  4. Verify the product is added correctly.
- **Expected Result**: Product is successfully added to the cart.

## 2. Regression Testing

### Test Case ID: TC_RT_001
- **Test Case Name**: Verify existing functionalities after new updates
- **Description**: Ensure that existing functionalities are not affected by new updates.
- **Pre-conditions**: Application has new updates.
- **Test Steps**:
  1. Execute previously passed functional test cases.
- **Expected Result**: All test cases pass successfully.

## 3. Integration Testing

### Test Case ID: TC_IT_001
- **Test Case Name**: Verify integration between login and inventory modules
- **Description**: Ensure that the login module correctly redirects to the inventory module.
- **Pre-conditions**: User is on the login page.
- **Test Steps**:
  1. Log in with valid credentials.
- **Expected Result**: User is redirected to the inventory page.

## 4. End-to-End Testing

### Test Case ID: TC_EE_001
- **Test Case Name**: Complete order placement workflow
- **Description**: Validate the complete workflow from user login to order placement.
- **Pre-conditions**: User is on the login page.
- **Test Steps**:
  1. Log in with valid credentials.
  2. Search for a product.
  3. Add the product to the cart.
  4. Proceed to checkout.
  5. Complete the checkout process.
- **Expected Result**: Order is placed successfully!
