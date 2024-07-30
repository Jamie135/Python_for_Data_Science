# ft_package

If "python3" command doesn't work, try "python"

## Build

```bash
python3 setup.py sdist bdist_wheel
```
or
```bash
python3 -m build
```
This will create the dist/ directory containing ft_package-0.0.1.tar.gz and ft_package-0.0.1-py3-none-any.whl

## Install

```bash
pip3 install ./dist/ft_package-0.0.1.tar.gz
```
or
```bash
pip3 install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## Display

```bash
pip3 show -v ft_package
```

## Test

```bash
python3 tester.py
```

## Uninstall

```bash
python3 uninstall.py
```

# Information

* `name`: The name of the package. This is the name that will be used to install the package.
* `version`: The version of the package. This is a string that uniquely identifies the version of the package.
* `description`: A brief description of the package. This description will be displayed when the user installs the package.
* `author`: The author of the package. This is the name of the person or organization that created the package.
* `author_email`: The author's email address. This is the email address that the user can contact if they have any questions about the package.
* `url`: The URL for the package's homepage. This is the URL where the user can find more information about the package.
* `packages`: A list of the directories that contain Python modules. This list tells the setuptools module where to find the Python modules that are included in the package.
* `classifiers`: A list of keywords that are used to categorize the package. These keywords are used by package managers to find packages that are relevant to the user's needs.
* `entry_points`: A list of console scripts for the package. These scripts can be run from the command line.
