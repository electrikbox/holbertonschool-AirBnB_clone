![](https://i.imgur.com/GM1iQ0P.png)

# <p align = "center">HolbertonBnB</p>

# <p align = "center">AirBnB Clone - The Console</p>

This is the first step towards building our first full web application: **the AirBnB clone**

For this project, we have focused on creating the console, which, as you can see from the diagram below, is the very first step and the basis of the Airbnb Clone projects to follow in the coming weeks

![](https://i.imgur.com/dtPVtVd.png)

## 🛠️ Console Setup
1. Clone this git repository

```bash
git clone https://github.com/ValPumpkins/holbertonschool-AirBnB_clone.git
cd holbertonschool-AirBnB_clone
```
2. You can now use the command interpreter

```basj
./console
```
3. If all goes well, the following prompt should appear

```bash
(hbtn)
```
4. You can now use it as you wish. The commands available are detailed below, in the "*Commands*" category.

### 💡 Bonus

This shell can also work in non-interactive mode :

```bash
echo "help" | ./console.py
```

## 🖲️ Commands
Once the console is open, you can type `help` to see all the commands available:
```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
```

| Commands | What it does | Usage |
| -------- | -------- | -------- |
| all    | Prints the string representations of all instances of a given class    | `all <class_name>` |
| create    | Creates a new instance of a given class, prints ID and save it into a JSON file   | `create <class_name>` |
| show    | Prints the string representation of a class instance based on a given id    | `show <class_name> <id>` |
| count    | Count the nb of instance of a given class    | `count <class_name>` |
| update    | Updates a class instance based on a given id with a given key/value attribute pair or dictionary of attribute pair    | `update <class name> <id> <attribute name> "<attribute value>"`
| destroy    | Deletes a class instance based on a given id    | `destroy <class_name> <id>` |
| help   |  Displays available commands or gives info  |  `help <command>`
| EOF    | Exit the console by EOF (`ctrl-D`)    | -
| quit    | Quit the console    | `quit`

### 💡 Alt syntax
You can also used every commands like that :
```bash
(hbnb) <class_name>.cmd(<optional arg>)
```
```bash
(hbnb) User.create()
1337
(hbnb) User.update(1337, name, Bernard)
```

### 📺 Outputs

- **create** :
```bash
(hbnb) create BaseModel
```
output ⤵️
```bash
bf68a684-6994-41cc-82f2-2d1341e711b3
```
- **show**
```bash
(hbnb) show BaseModel bf68a684-6994-41cc-82f2-2d1341e711b3
```
output ⤵️
```bash
[BaseModel] (bf68a684-6994-41cc-82f2-2d1341e711b3) {'id': 'bf68a684-6994-41cc-82f2-2d1341e711b3', 'created_at': datetime.datetime(2023, 11, 1, 17, 44, 6, 792332), 'updated_at': datetime.datetime(2023, 11, 1, 17, 44, 6, 792371)}
```
- **count**
```bash
(hbnb) count User
```
output ⤵️
```bash
2
```
- **update**
```bash
(hbnb) update BaseModel bf68a684-6994-41cc-82f2-2d1341e711b3 name "Roger"
```
output ⤵️
```bash
no output
```
but `file.json` is updated :
```json
{
	"BaseModel.bf68a684-6994-41cc-82f2-2d1341e711b3": {
        "id": "bf68a684-6994-41cc-82f2-2d1341e711b3",
        "created_at": "2023-11-01T17:44:06.792332",
        "updated_at": "2023-11-01T17:48:32.407856",
        "name": "Roger",
        "__class__": "BaseModel"
    }
}
```
- **destroy**
```bash
(hbnb) destroy BaseModel bf68a684-6994-41cc-82f2-2d1341e711b3
```
output ⤵️
```bash
no output
```
but `file.json` is updated :
```json
{}
```

## 🗃️ Classes
### 👑 BaseModel
The **BaseModel class** is the base class for this project and defines all the attributes for the other classes

| Public instance attributes | Public instance methods |
| -------- | -------- |
| `id`    | `save`   |
| `created_at`    | `to_dict`    |
| `updated_at`    | -    |

### 👶 Others Classes
#### 🚨 Inherits  from `BaseModel`

| Class names | Public Class Attributes |
| -------- | -------- |
| User   | `email`  / `password` / `first_name` / `last_name`      |
| State    | `name`   |
| City    | `state_id` / `name`    |
| Amenity    | `name`    |
| Place    | `city_id`  / `user_id` / `name` / `description` / `number_rooms` / `number_bathrooms` / `max_guest` / `price_by_night` / `latitude` / `longitude` / `amenity_ids`    |
| Review    | `place_id` / `user_id` / `text`    |


### 📦 Storage
The `FileStorage` class is used to save and load data from a JSON file.

It acts as a bridge between the application's objects and a file, ensuring data persistence, it allows the application to store and retrieve instances of various classes efficiently.

| Public instance methods | Private class attributes |
| -------- | -------- |
| `all`    | `file_path`    |
| `new`   | `objects`   |
| `save`    | -    |
| `reload`    | -    |

## 💪 Testing
Unittests for this project are defined in the `tests` folder.
You can run the entire test suite by using the following command :
```bash
python3 -m unittest discover tests
```
or you can run the test file by file with this command :
```bash
python3 -m tests/test_models/test_base_model.py
```
To date, here are the results of our tests :
```bash
...................
----------------------------------------------------------------------
Ran 19 tests in 0.008s

OK
```

### ☂️ Coverage

```bash
Name                            Stmts   Miss Branch BrPart  Cover
-----------------------------------------------------------------
models/amenity.py                   4      0      0      0   100%
models/base_model.py               28      0      8      0   100%
models/city.py                      5      0      0      0   100%
models/engine/file_storage.py      33      0      8      0   100%
models/place.py                    14      0      0      0   100%
models/review.py                    6      0      0      0   100%
models/state.py                     4      0      0      0   100%
models/user.py                      7      0      0      0   100%
-----------------------------------------------------------------
TOTAL                             101      0     16      0   100%
```

## 👥 Team
- 🥁 Olive t'Servrancx aka [electrikbox](https://github.com/electrikbox)
- 🥦 Valentine Quignon aka [ValPumpkins](https://github.com/ValPumpkins)

## © License
This project is licensed under the **MIT License** - see the `LICENSE` file for details.
