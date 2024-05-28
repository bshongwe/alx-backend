# 🌐 0x02. i18n
`Backend`</br>
Welcome to the **0x02. i18n** project! This project focuses on
internationalization (i18n) in the back-end using Flask. The aim is to make
applications adaptable to different languages and regions.
<br></br>

## 📚 Resources
Read or watch:
- [Flask-Babel](https://pythonhosted.org/Flask-Babel/)
- [Flask i18n tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)
- [pytz](http://pytz.sourceforge.net/)
<br></br>

## 🎯 Learning Objectives
- 📝 Learn how to parametrize Flask templates to display different languages.
- 🌎 Learn how to infer the correct locale based on URL parameters, user
settings, or request headers.
- ⏰ Learn how to localize timestamps.
<br></br>

## ✅ Requirements
- 🐧 All your files will be interpreted/compiled on Ubuntu 18.04 LTS using
Python 3 (version 3.7).
- 📝 All your files should end with a new line.
- 📄 A `README.md` file, at the root of the folder of the project, is
mandatory.
- 🧑‍💻 Your code should use the `pycodestyle` style (version 2.5).
- 🏷️ The first line of all your files should be exactly
`#!/usr/bin/env python3`.
- 📂 All your `.py` files should be executable.
- 📝 All your modules should have documentation.
- 📝 All your classes should have documentation.
- 📝 All your functions and methods should have documentation.
- 🏷️ All your functions and coroutines must be type-annotated.
<br></br>

## 🚀 Tasks

| Task Name                             | Files                                                                                                          | Description                                                                                                                                                            |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **0. Basic Flask app**                | `0-app.py`, `templates/0-index.html`                                                                           | Create a basic Flask app with a single `/` route and an `index.html` template that displays “Welcome to Holberton” as the page title and “Hello world” as the header.  |
| **1. Basic Babel setup**              | `1-app.py`, `templates/1-index.html`                                                                           | Install Flask-Babel, instantiate the Babel object, configure available languages, set the default locale and timezone, and use the configuration for your Flask app.   |
| **2. Get locale from request**        | `2-app.py`, `templates/2-index.html`                                                                           | Create a `get_locale` function to determine the best match with supported languages using `request.accept_languages`.                                                  |
| **3. Parametrize templates**          | `3-app.py`, `babel.cfg`, `templates/3-index.html`, `translations/en/LC_MESSAGES/messages.po`, `translations/fr/LC_MESSAGES/messages.po`, `translations/en/LC_MESSAGES/messages.mo`, `translations/fr/LC_MESSAGES/messages.mo` | Parametrize your templates using `_` or `gettext`. Initialize and compile translations for English and French.                                                         |
| **4. Force locale with URL parameter**| `4-app.py`, `templates/4-index.html`                                                                           | Implement a way to force a particular locale by passing the `locale` parameter in the URL.                                                                             |
| **5. Mock logging in**                | `5-app.py`, `templates/5-index.html`                                                                           | Emulate user login by using a user table and mock logging in via the `login_as` URL parameter. Display a welcome message if the user is logged in.                     |
| **6. Use user locale**                | `6-app.py`, `templates/6-index.html`                                                                           | Update `get_locale` to use the user’s preferred locale if supported, with priority: URL parameters, user settings, request header, and default locale.                 |
| **7. Infer appropriate time zone**    | `7-app.py`, `templates/7-index.html`                                                                           | Define a `get_timezone` function to select the time zone based on URL parameters, user settings, and default to UTC. Validate the time zone using `pytz`.              |

<br></br>
## 🛠️ Setup
### 📋 Prerequisites
- Python 3.7
- Flask
- Flask-Babel
- pytz
<br></br>

## 🤝 Contributing
Contributions are welcome as this is an educational repo

1. Create your Contribution Branch (`git checkout -b feature/ContributionFeature`)
2. Commit your Changes (`git commit -m 'Add some ContributionFeature'`)
3. Push to the Branch (`git push origin feature/ContributionFeature`)
4. Open a Pull Request
<br></br>

## 📄 License
TBA
<br></br>

## 🙏 Acknowledgements
- 🌟 [Flask-Babel Documentation](https://pythonhosted.org/Flask-Babel/)
- 📚 [Flask i18n tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)
- 💻 [pytz Documentation](http://pytz.sourceforge.net/)


