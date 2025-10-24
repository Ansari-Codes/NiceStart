# NiceStart 👌
> A way to assemble your niecgui project nicely ✨👌

## Background:
👋 Hey there! I’m Muhammad Abubakar Siddique Ansari, a passionate Python, Laravel, and Vue.js developer.

I’ve explored many frameworks for web development, but one that truly caught my attention in Python’s world was NiceGUI — it felt elegant, modern, and powerful.

Later, as I learned Laravel and Vue.js, I realized something interesting:

> PHP became popular largely because Laravel made it shine.

That sparked an idea 💡 —
What if Python had something like that too? A framework ecosystem that’s as smooth, developer-friendly, and production-ready as Laravel — but Python-native? Nicegui already gave web power to python, but lacks structure. Also, lacks starterkits, premade setups, extensions and more.

That’s where my vision begins:
🚀 **NiceStart** **— a starter kit for NiceGUI projects**.
A framework foundation designed to give Python web developers the same joy, structure, and efficiency that Laravel offers to PHP developers.

## Directory Structure:
Default directory looks like that:
```
Project
├── backend
│   ├── _query.py
│   └── Auth.py
├── comps
│   └── Welcome
│       ├── CompHero.py
│       ├── CompFooter.py
│       └── CompHeader.py
├── db
├── pages
│   ├── Auth
│   │   ├── PageLogin.py
│   │   ├── PageSignUp.py
│   │   └── PageDashboard.py
│   └── PageWelcome.py
├── routes
│   ├── __init__.py
│   ├── RouteAuth.py
│   ├── ROUTES.py
│   └── RouteWeb.py
├── UI
│   ├── __init__.py
│   ├── Basic.py
│   ├── Raw.py
│   └── Theme.py
├── utils
│   ├── __init__.py
│   ├── Auth.py
├── ENV.py
├── MAIN.py
├── README.md
└── requirements.txt
```

### 1. Backend: 
This folder contains files that has no concern with ui. This folder defines real functionality of app. Defaultly, it contains:

1. `_query.py`: The file defines functions to query from database.
2. `auth.py`: The file that defines functionality for authentication.

**Naming:** Always snake case (spaces replaced by underscore and lower case). For the files which has to act as "Local Utility", like _query.py, which has to work only in backend folder, should be started from underscore.

### 2. Comps
This folder contains reusable components which are used in pages. Defaults:

1. `Welcome/*`: This folder contains files;
    - `CompHero.py`: Creates Hero section of welcome page.
2. `CompHeader.py`: This file contains Header component.
3. `CompFooter.py`: This file contains Footer component.

**File Structure:** Each file contains a function named as same as the file. Like in `CompHero.py`, the function which is to be used is **`CompHero()`**. 

**Naming**: The file name starts from Comp and first letter of other parts is always capital. Like camel case but first letter also captial!

### 3. Db
...

### 4. Pages
This directory contains actual pages. Defaults:

1. `Auth/*`: This folder contains two files;
    - `PageLogin.py`: Defines login page.
    - `PageSignUp.py`: Defines signup page.
2. `PageDashboard`: File showing premade dashboard.
3. `PageWelcome`: Welcome Page.

**File Structure:** Each file contains one create function where acutal content of the file is to be served over routes.

**Naming:** Naming a file is same as Comps with the difference that here, you have to use **Page prefix** instead of Comps. 