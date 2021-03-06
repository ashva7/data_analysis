from setuptools import setup, find_packages

setup(
	name = 'data_analysis',
	version = '0.0.1',
	url = 'https://github.com/ashva7/data_analysis',
	license = 'BSD',
	author = 'Ashwini Verma',
	packages = find_packages(),
	install_requires =     [#'PyQt5', 
				'pandas', 
				'sqlalchemy', 
				'nltk', 
				'numpy', 
				'jupyter', 
				'python-twitter'],
	entry_points = {},
	extras_require = {'dev': ['flake8',]},
	)
