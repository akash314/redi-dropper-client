# Change Log


## [0.2.0] - 2016-10-11

### New Features
 * Admin Users can edit existing users.
 * Deleter users can delete files that exist.
 * The dashboard is easier to search.

### Changed
 * Fixes for pagination. (Patrick White)
 * Use config to find out where the deleted files are (Patrick White)
 * Delete File changes and additions (Patrick White)
 * Fixed dashboard presentation. (Patrick White)
 * Update README.md (Kevin Hanson)
 * deploy/fabfile.py enhancement to allow for easy database upgrades and downgrades (Patrick White)
 * Made both the app/fabfile.py and bootstrap_functions.sh apply the most recent database version. (Patrick White)
 * Edit user logging (ndavuluri)
 * Unit tests and client side edit form changes (Patrick White)
 * UserID and Role should be unique, adding an Unique Index for usrID,rolID. (ndavuluri)
 * Only Admin User is allowed to create and edit User (ndavuluri)
 * Polling for new subject data (Patrick White)
 * Filter function for dashboard subject search (Patrick White)
 * Initial Changes for Edit User:Adding a new route and updating db and loging (ndavuluri)
 * Edit user changes (Patrick White, ndavuluri)


## [0.1.2] - 2016-04-13

### Changed
 * Minor fix for js/utils.py to increase max upload filesize from 1gb to 3gb (Kevin S. Hanson)



## [0.1.1] - 2016-04-07

### Changed
 * Minor fix for utils.py to ignore certificate error in curl statement (Christopher P. Barnes)



## [0.1.0] - 2016-02-05

### Changed
 * Improve logging: show the shib email (Andrei Sura)
 * docs/README.md: list variables that need to be changed for deployment (Andrei Sura)



## [0.0.4b] - 2016-02-08

### Changed
* Try runnning `pip` as `www-data` to avoid fixing permissions (Andrei Sura)



## [0.0.4a] - 2016-02-05

 * Use sudo for `pip install` during deployment (Andrei Sura)
 * Minor fixes for sample.fabric.py (Andrei Sura)
 * Update docs/README.md formatting (Andrei Sura)
 * Add mkdocs.yml (Andrei Sura)
 * Update .gitignore (Andrei Sura)
 * Save older documentation files (needs some polishing) (Andrei Sura)
 * Improve pattern matching for fabric task `check_app` (Andrei Sura)
 * Fix "TypeError: can't compare datetime.datetime to NoneType" in user_entity.py (Andrei Sura)
 * Make parallax page responsive (Ruchi Vivek Desai)
 * Change right angle icon on top navigation bar to menu icon (Ruchi Vivek Desai)
 * update changelog for release 0.0.3b (Ruchi Vivek Desai)



## [0.0.4] - 2016-01-21

### Added
* Add app/deploy/sample.virtualhost-ssl.conf because we need two apache config files (Andrei Sura)
* Add support for saving the user email as a password (no password field is currently displayed)
    Note: This password will be checked only if "local auth" is used (Andrei Sura)
* Add doi link (Andrei Sura)

### Changed
* Rename `sample.vagrant.settings.conf` => `sample.vagrant.settings.conf` (Andrei Sura)
* Remove space in app/deploy/sample.virtualhost.conf (Andrei Sura)
* Rename `sample.settings.conf` -> sample.vagrant.settings.conf to properly refrlect the file's function (Andrei Sura)
* Move config files to dot_files/aliases (Andrei Sura)



# [0.0.3b] - 2015-08-31

### Changed
* Add option for accepting parent repo path (Ruchi Vivek Desai)
* Restore click functionality for main page "getting started" (Andrei Sura)
* Simplify sample.virtualhost.conf used on prod (Andrei Sura)


## [0.0.3a] - 2015-08-27

### Added
* Add sample config files for deploying two application instances
Paths ==> `/alz` and `/onefl` (Andrei Sura)

## [0.0.3] - 2015-08-26

### Fixed
* Issue #109 - AttributeError: 'NoneType' object has no attribute 'email' (Andrei)

### Changed
* Update AUTHORS.md (Andrei)

### Added
* Add sections for getting started, faq and support (Ruchi Vivek Desai)


## [0.0.2a] - 2015-08-20

### Added
 * adding authors file (Kevin Steven Hanson)

## [0.0.2] - 2015-08-18

### Fixed
* Fix issue with settings.conf not linked when doing `vagrant up` + improve docs/README.md (Andrei Sura)
* Fix issue #104 and add tests for it (Ruchi Vivek Desai)
* Fix issue #44 - parallax the login page (Ruchi Vivek Desai)
* Fix issue #75 - cURL max time (configurable in settings.conf with `REDCAP_CURL_API_MAX_TIME` (Andrei Sura)
* Fix issue #73 - show user email instead of id in logs  (Andrei Sura)

### Removed
* Remove duplicate vagrant to avoid confusion (Andrei Sura)

### Changed
* Make "upload box" larger - related to issue #34 (Andrei Sura)
* Change sed call to work with BSD and GNU versions (Taeber Rapczak)

### Added
* Added bootstrap parallax design to `prototype` dir for later integration (Kevin Steven Hanson)


## [0.0.1c] - 2015-07-23

### Fixed
* Fix bugs in deployment script (Andrei Sura)


## [0.0.1b] - 2015-07-21

### Fixed
* Display APP_VERSION in the footer (fixes issue #74 ) (Andrei Sura)
* Fix deploy/fabfile.py to properly reference the 'current' requirements (Andrei Sura)
* Check if the tag number is valid during deployment (Andrei Sura)


## [0.0.1a] - 2015-07-21

### Added
* Add '-t tag_number' to app/README.rst (Andrei Sura)
* Add the missing CHANGELOG.md (Andrei Sura)

### Fixed
* Fix for issue #86 - specify tag number for deployment $ ./deploy.sh -i -t 0.0.1 (Andrei Sura)
* Fix remove conversion to int for `redcap_id` (Andrei Sura)


## [0.0.1] - 2015-07-18

### Added
* Save code with working deployment script


## [0.0.0] - 2015-03-13
### Added
* Initial commit with a one line README.md
