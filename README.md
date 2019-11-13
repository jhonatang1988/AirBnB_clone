# AirBnB clone project!

## Description

The AirBnb_clone Project is the part number 1 of a series of projecs we will do in our process to become Full-Stack Software Engineers. This first phase consists in a custom cummand-line interface that allow to us create, update an delete instances of different classes. Also AirBnB project has a storage class and a BaseModel class that allow to console do its work.

## Usage
The console works in interactive an non-interactive mode, like unix shell. It prints the promp (hbnb) and waits and instruction:

Command                  | Example
--------                 | -------------
Run the console          | ./console.py
Quit the console         | (hbnb) quit
Display the help         | (hbnb) help <command>
Create an object         | (hbnb) create <class>
Show an object           | (hbnb) show <class> <id> or (hbnb) <class>.show(<id>)
Destroy an object        | (hbnb) destroy <class> <id> or (hbnb) <class>.destroy(<id>)
Show all objects         | (hbnb) all or (hbnb) all <class>
Update an object         | (hbnb) update <class> <id> <attribute name> "<attribute value>"

## Non-interactive mode example

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
```

## Interactive mode example
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
## Models

File                     | Description                                                  | Attributes
------------------------ | -------------------------------------------------------------|----------------------------------------------------|
base_model.py            | BaseModel class for all the other classes                    | id, created_at, updated_at                         |
user.py                  | User class for future user information                       | email, password, first_name, last_name             |
amenity.py               | Amenity class for future amenity information                 | name                                               |
city.py                  | City class for future location information                   | state_id, name                                     |
state.py                 | State class for future location information                  | name                                               |
place.py                 | Place class for future accomodation information              | city_id, user_id, name, description, number_rooms, |
place.py                 | Place class for future accomodation information              | number_bathrooms,max_guest, price_by_night,        |
place.py                 | Place class for future accomodation information              | latitude, longitude, amenity_ids.                  | 
review.py                | Review class for future user/host review information         | place_id, user_id, text                            |


## File Storage

The folder engine manages the serialization adn deserialization of all data.
The class is defined in file_storage.py with methods to follow this:<object> -> to_dict() -> <dictionary> -> JSON dump -> <json string> -> FILE -> <json string> -> JSON load -> <dictionary> -> <object>

The init.py file contains the instantiation of the FileStorage class called storage, followed by a call to the method reload() on that instance. This allows the storage to be reloaded automatically at initialization, which recovers the serialized data.

## Tests

All the code is tested with the unittest module. 

## Authors

- Jhonatan Galindo - jhonatan1988@gmail.com
- Karen Herrera - karenahv@gmail.com