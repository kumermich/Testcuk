# Firebase Code Example - Files

# 
# Here's an example of how you can use Firebase to upload and download files
#

import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

# Initialize the Firebase Admin SDK
cred = credentials.Certificate('path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'your-storage-bucket-url.appspot.com'
})

# Upload a file to Firebase Storage
def upload_file(file_path, destination_path):
    bucket = storage.bucket()
    blob = bucket.blob(destination_path)
    blob.upload_from_filename(file_path)
    print('File uploaded successfully.')

# Download a file from Firebase Storage
def download_file(file_name, destination_path):
    bucket = storage.bucket()
    blob = bucket.blob(file_name)
    blob.download_to_filename(destination_path)
    print('File downloaded successfully.')

# Example usage
upload_file('path/to/local/file.jpg', 'images/file.jpg')
download_file('images/file.jpg', 'path/to/local/downloaded_file.jpg')