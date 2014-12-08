from distutils.core import setup

setup(
	name = 'pybursts',
	packages = ['pybursts'], # this must be the same as the name above
	version = '0.1.1',
	description = 'A Python port from the \'burst detection\' algorithm by Kleinberg, originally implemented in R',
	author = 'Renzo Poddighe',
	author_email = 'poddighe.renzo@gmail.com',
	url = 'https://github.com/rpoddighe/pybursts', # use the URL to the github repo
	download_url = 'https://github.com/rpoddighe/pybursts/tarball/0.1.1', # I'll explain this in a second
	keywords = ['burst detection', 'data mining', 'text mining'], # arbitrary keywords
	classifiers = [],
)