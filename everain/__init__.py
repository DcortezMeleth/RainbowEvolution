# coding=utf-8
import logging
import sys
import yaml

__author__ = 'Bartosz Sądel'

try:
    params = yaml.safe_load(open('resources/config.yml'))
    logging.basicConfig(format=params['logging']['format'], filename=params['logging']['path'])
    print "Product types: " + str("Logging initialized!")
except IOError as error:
    print 'Error while loading configuration file:\n' + str(error)
    sys.exit()
