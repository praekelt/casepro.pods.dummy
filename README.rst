casepropods.dummy
==================

Example casepro data pod returning statically configured data.

Install
~~~~~~~

.. code-block::

  $ pip install casepropods.dummy

Usage
~~~~~

In casepro's settings file, add the pod as an installed app, and configure the pods that you would like to show in the UI:

.. code-block:: python

  INSTALLED_APPS += ('casepropods.dummy.plugin.DummyPodPlugin',)

  PODS = [{
      'label': 'dummy_pod',
      'title': 'Maternal Health Info',
      'data': {
          'items': [{
              'name': 'EDD',
              'value': '2015-07-18'
          }, {
              'name': 'Clinic Code',
              'value': '2034 6524 6421'
          }]
      }
  }, {
      'label': 'custom_pod',
      'title': 'Custom Info',
  }]
