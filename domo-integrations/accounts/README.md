```The files in these examples are read only. To execute the files you will need to copy + paste the code, or download the files and upload them into your workspace.```

# Use Domo Accounts in Jupyter

Example of how to use a Domo account in a Jupyter Notebook

## Files
- exampleAccount.ipynb - A Jupyter notebook with a simple example of using accounts in a notebook

## Instructions

#### Before running your workspace

1. When creating or updating a workspace choose the optional step "Accounts"
2. Select the button "Add Account"
3. Choose an Account

Optionally, give the account a different alias

4. Click "Save Workspace" to apply your account

### After updating/creating a workspace

1. Start your workspace
2. Create a new notebook (or update an existing notebook)
3. On the left navigation there is an account icon
    - Use this to view the accounts you have configured for the workspace
    - Optionally double-click on the account alias to pre-populate starting code to use the account. Skip step 4 
4. Import the domojupyter asset
    - `import domojupyter as domo`

## Getting account information
* Get properties on the account
    * `account_properties = domo.get_account_property_keys('account_name')`
* Get value of an account property
    * `account_property_value = domo.get_account_property_value('account_name', 'property_name')`


