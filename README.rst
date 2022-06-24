Nevua 
~~~~~

This is a platform for disease forcasting. It is especially focused on monitoring the COVID-19 outbreak.

Currently includes:

* A dashboard that detects hotspots based on growth (not total cases) and maps them.

Uses third-party data:

* Coronavirus data from the New York Times.

This is a reboot of an old project from the start of the pandemic. We are forking it to get it into a publishable form for an academic venue.

Installation
~~~~~~~~~~~~

:: 

    pip install nevua


Usage
~~~~~

::

    nevua up

Running the web app on a WSGI server is recommended for production. The module is 
"nevua.app:SERVER". We use uWSGI.


License and Credits
~~~~~~~~~~~~~~~~~~~

Apache Licensed. 
Forked from corona-dashboard project of B.Next which had same author (JJ Ben-Joseph).