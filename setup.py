#!/usr/bin/env python

from distutils.core import setup

setup(name='MySensors',
      version='1.0',
      description='MySensors serial decoders',
      author='Brenda Wallace',
      author_email='brenda@wallcae.net.nz',
      url='https://allthethings.nz/',
      packages=['mysensors', 'mysensors.gateways'],
     )