from setuptools import setup, find_packages

setup(
  name = 'hebpipe',
  packages = find_packages(),
  version = '0.9.0.0',
  description = 'A pipeline for Hebrew NLP',
  author = 'Amir Zeldes',
  author_email = 'amir.zeldes@georgetown.edu',
  package_data = {'':['README.md','LICENSE.txt'],'hebpipe':['lib/*','data/*','bin/*']},
   install_requires=['scikit-learn==0.19.0'],
  url = 'https://github.com/amir-zeldes/HebPipe',
  license='Apache License, Version 2.0',
  download_url = 'https://github.com/amir-zeldes/HebPipe/releases/tag/v0.9.0.0',
  keywords = ['NLP', 'Hebrew', 'segmentation', 'tokenization', 'tagging', 'parsing'],
  classifiers = ['Programming Language :: Python',
'Programming Language :: Python :: 2',
'Programming Language :: Python :: 3',
'License :: OSI Approved :: Apache Software License',
'Operating System :: OS Independent'],
)