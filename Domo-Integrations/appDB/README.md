# Use AppDB in Jupyter

Example of how to use AppDB in a Jupyter Notebook

## Files
- exampleAppDB.ipynb - A Jupyter notebook with a simple example of using appDB in a notebook

## Instructions

#### Before running your workspace

1. When creating or updating a workspace choose the optional step "AppDB Collections"
2. Select the button "Add Collection"
3. Choose a collection

Optionally, give the collection a different alias

4. Click "Save Workspace" to apply your collection(s)

### After updating/creating a workspace

1. Start your workspace
2. Create a new notebook (or update an existing notebook)
3. On the left navigation there is an appDB icon
    - Use this to view the appDB collections you have configured for the workspace
    - Optionally double-click on the collection alias to pre-populate starting code to use the collection. Skip step 4 
4. Import the domojupyter asset
    - `import domojupyter.app_db as app_db`

## Functions
* Get list of documents
    * `app_db.get_documents('collection_name', offset:number, limit:number)`
* Get document by id
    * `app_db.get_document('collection_name', document_id)`
* Update a document
    * `app_db.update_document('collection_name', document)`
* Update a list of documents
    * `app_db.update_documents('collection_name', documents)`
* Delete document by id
    * `app_db.delete_document('collection_name', document_id)`
* Delete a list of documents
    * `app_db.delete_documents('collection_name', documentIdsToDelete)`
* Create a document
    * `app_db.create_document('collection_name', newDocument)`
* Create a list of documents
    * `app_db.create_documents('collection_name', newDocuments)`