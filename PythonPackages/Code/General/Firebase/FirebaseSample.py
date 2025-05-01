# Firebase Code Example

# 
# Here's a code example that demonstrates how to use Firebase Realtime Database in Python
# In the above example, we first initialize the Firebase Admin SDK using a service account key file (serviceAccountKey.json) and specify the database URL ('https://your-project.firebaseio.com/'). You need to replace 'your-project' with the actual name of your Firebase project.
#

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize the Firebase Admin SDK
cred = credentials.Certificate('path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-project.firebaseio.com/'
})

# Get a reference to the root of the Firebase Realtime Database
ref = db.reference()

# Write data to the database
ref.child('users').child('001').set({
    'name': 'John Doe',
    'age': 30,
    'email': 'johndoe@example.com'
})

# Read data from the database
users_ref = ref.child('users')
snapshot = users_ref.get()
for user_id, user_data in snapshot.items():
    print(f"User ID: {user_id}")
    print(f"Name: {user_data['name']}")
    print(f"Age: {user_data['age']}")
    print(f"Email: {user_data['email']}")
    print()

# Update data in the database
ref.child('users').child('001').update({
    'age': 31,
    'email': 'john.doe@example.com'
})

# Delete data from the database
ref.child('users').child('001').delete()